const cache = new Map();
const pending = new Map();
export async function videoAvailability(id) {
  if (!/^[A-Za-z0-9_-]{11}$/.test(id || '')) return { status: 'unavailable', reason: 'invalid_id' };
  const saved = cache.get(id);
  if (saved && saved.expires > Date.now()) return saved.value;
  if (pending.has(id)) return pending.get(id);
  const work = (async () => {
    let value;
    try {
      const url = new URL('https://www.youtube.com/oembed');
      url.search = new URLSearchParams({ url: 'https://www.youtube.com/watch?v=' + id, format: 'json' }).toString();
      const response = await fetch(url, { signal: AbortSignal.timeout(5500), redirect: 'error' });
      if (response.ok) {
        const data = await response.json();
        value = data.type === 'video' && typeof data.title === 'string' && /youtube(?:-nocookie)?\.com\/embed\//.test(data.html || '') ? { status: 'available', title: data.title.slice(0, 240), author: String(data.author_name || '').slice(0, 150) } : { status: 'unconfirmed', reason: 'invalid_metadata' };
      } else value = [400,401,403,404,410].includes(response.status) ? { status: 'unavailable', reason: 'private_removed_or_embedding_restricted' } : { status: 'unconfirmed', reason: 'provider_unavailable' };
    } catch { value = { status: 'unconfirmed', reason: 'verification_failed' }; }
    value.checkedAt = new Date().toISOString();
    if (cache.size >= 500) cache.delete(cache.keys().next().value);
    cache.set(id, { value, expires: Date.now() + (value.status === 'unconfirmed' ? 15000 : 300000) });
    return value;
  })().finally(() => pending.delete(id));
  pending.set(id, work);return work;
}
