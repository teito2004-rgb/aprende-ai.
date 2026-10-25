import { extractChapters, chapterClip } from './video-chapters.js';
// Public captions only. No login, audio download, proxy rotation or bot bypass.
const evidenceCache = new Map();
export function youtubeId(value) {
  try {
    const u = new URL(value);
    if (u.protocol !== 'https:') return null;
    const id = u.hostname === 'youtu.be' ? u.pathname.slice(1) : /(^|\.)youtube\.com$/.test(u.hostname) ? u.searchParams.get('v') || u.pathname.match(/^\/(?:shorts|embed)\/([^/]+)/)?.[1] : null;
    return /^[\w-]{11}$/.test(id || '') ? id : null;
  } catch { return null; }
}
export function playerData(html, variable = 'ytInitialPlayerResponse') {
  const marker = (variable === 'ytInitialData' ? /(?:var\s+)?ytInitialData\s*=\s*/ : /(?:var\s+)?ytInitialPlayerResponse\s*=\s*/).exec(html);
  if (!marker) return null;
  const start = marker.index + marker[0].length;
  let depth = 0, quoted = false, escaped = false;
  for (let i = start; i < html.length; i++) {
    const c = html[i];
    if (quoted) { if (escaped) escaped = false; else if (c === '\\') escaped = true; else if (c === '"') quoted = false; }
    else if (c === '"') quoted = true;
    else if (c === '{') depth++;
    else if (c === '}' && --depth === 0) { try { return JSON.parse(html.slice(start, i + 1)); } catch { return null; } }
  }
  return null;
}
export function normalizeCues(items, milliseconds = false) {
  const scale = milliseconds ? 1000 : 1;
  return items.flatMap(item => {
    const start = Number(item.start ?? item.offset ?? item.tStartMs) / scale;
    const duration = Number(item.duration ?? item.dDurationMs) / scale;
    const text = typeof item.text === 'string' ? item.text : item.segs?.map(s => s.utf8 || '').join('') || '';
    const cleaned = text.replace(/\s+/g, ' ').trim().slice(0, 1500);
    return Number.isFinite(start) && start >= 0 && Number.isFinite(duration) && duration > 0 && cleaned ? [{ start, end: start + duration, text: cleaned }] : [];
  }).sort((a, b) => a.start - b.start).slice(0, 2000);
}
export function transcriptBlocks(cues) {
  const blocks = [];
  for (const cue of cues) {
    const previous = blocks.at(-1);
    if (previous && cue.start - previous.start < 12 && previous.text.length + cue.text.length < 420) {
      previous.end = Math.max(previous.end, cue.end); previous.text += ' ' + cue.text;
    } else blocks.push({ id: 't' + blocks.length, start: cue.start, end: cue.end, text: cue.text });
  }
  // Preserve coverage throughout longer videos rather than only reading the intro.
  if (blocks.length <= 75) return blocks;
  return Array.from({ length: 75 }, (_, i) => blocks[Math.floor(i * (blocks.length - 1) / 74)]);
}
async function boundedText(url, signal, limit) {
  const response = await fetch(url, { signal, redirect: 'error' });
  if (!response.ok) return null;
  if (Number(response.headers.get('content-length')) > limit) { await response.body?.cancel(); return null; }
  const reader = response.body?.getReader(); if (!reader) return null;
  const parts = []; let size = 0;
  try {
    while (true) { const { value, done } = await reader.read(); if (done) break; size += value.length; if (size > limit) { await reader.cancel(); return null; } parts.push(value); }
  } finally { reader.releaseLock(); }
  const bytes = new Uint8Array(size); let offset = 0; for (const part of parts) { bytes.set(part, offset); offset += part.length; }
  return new TextDecoder().decode(bytes);
}
export async function videoEvidence(source, parentSignal) {
  const id = youtubeId(source.url); if (!id) return source;
  const cached = evidenceCache.get(id);
  if (cached && cached.expires > Date.now()) return { ...source, ...cached.value };
  const signal = AbortSignal.any([parentSignal, AbortSignal.timeout(9000)]);
  let chapters = [], cues = [], language = '', durationSeconds = null, captionStatus = 'unavailable', reason = 'public_captions_not_retrieved', provider = 'youtube-public';
  try {
    const html = await boundedText('https://www.youtube.com/watch?v=' + id, signal, 3500000);
    const player = html ? playerData(html) : null;
    const duration = Number(player?.videoDetails?.lengthSeconds);
    if (Number.isFinite(duration) && duration > 0) durationSeconds = duration;
    if(player)chapters = extractChapters({ videoDetails:player.videoDetails, player, initialData:playerData(html,'ytInitialData') },durationSeconds);
    const tracks = player?.captions?.playerCaptionsTracklistRenderer?.captionTracks || [];
    const track = tracks.find(t => /^pt/.test(t.languageCode)) || tracks.find(t => /^en/.test(t.languageCode)) || tracks[0];
    if (player?.playabilityStatus?.status === 'OK' && track?.baseUrl) {
      const u = new URL(track.baseUrl);
      if (u.protocol === 'https:' && ['youtube.com', 'www.youtube.com'].includes(u.hostname) && u.pathname === '/api/timedtext' && !u.username && !u.password && !u.port) {
        u.searchParams.set('fmt', 'json3');
        const body = await boundedText(u.href, signal, 1500000);
        if (body) { const raw = JSON.parse(body); cues = normalizeCues(raw.events || [], true); language = track.languageCode || ''; }
      }
    }
  } catch { captionStatus = signal.aborted ? 'timeout' : 'unavailable'; }
  // Optional documented native-caption provider. Never generates/transcribes audio.
  if (!cues.length && process.env.SUPADATA_API_KEY && !parentSignal.aborted) {
    provider = 'supadata-native';
    try {
      const url = new URL('https://api.supadata.ai/v1/transcript');
      url.search = new URLSearchParams({ url: 'https://www.youtube.com/watch?v=' + id, lang: 'pt', text: 'false', mode: 'native' }).toString();
      const response = await fetch(url, { headers: { 'x-api-key': process.env.SUPADATA_API_KEY }, signal: AbortSignal.any([parentSignal, AbortSignal.timeout(8000)]), redirect: 'error' });
      if (response.status === 200) { const raw = await response.json(); cues = normalizeCues(Array.isArray(raw.content) ? raw.content : [], true); language = raw.lang || ''; reason = cues.length ? 'ok' : 'provider_empty'; }
      else reason = 'provider_http_' + response.status;
    } catch { reason = 'provider_request_failed'; }
  }
  const blocks = transcriptBlocks(cues);
  const value = { chapters, durationMinutes: durationSeconds ? durationSeconds / 60 : null, durationSeconds, transcript: { status: blocks.length ? 'available' : captionStatus, language, provider, reason: blocks.length ? 'ok' : reason, blocks } };
  if (evidenceCache.size >= 80) evidenceCache.delete(evidenceCache.keys().next().value);
  evidenceCache.set(id, { value, expires: Date.now() + (blocks.length ? 21600000 : 600000) });
  return { ...source, ...value };
}
export function verifiedClip(source, selection, maxSeconds) {
  if (!selection || typeof selection !== 'object') return null;
  if (source.transcript?.status !== 'available' || !Array.isArray(source.transcript.blocks)) return chapterClip(source,selection,maxSeconds);
  const blocks = source.transcript.blocks;
  const from = blocks.findIndex(b => b.id === selection.from);
  const to = blocks.findIndex(b => b.id === selection.to);
  if (from < 0 || to < from) return null;
  // Sampled-out passages cannot be silently treated as having been read.
  for (let i = from; i < to; i++) if (Number(blocks[i + 1].id.slice(1)) !== Number(blocks[i].id.slice(1)) + 1) return null;
  const start = Math.floor(blocks[from].start), end = Math.ceil(blocks[to].end);
  if (end <= start || end - start > maxSeconds || (source.durationSeconds && end > Math.ceil(source.durationSeconds))) return null;
  return { startSeconds: start, endSeconds: end, basis: 'transcript', language: source.transcript.language, label: 'Trecho selecionado pela transcrição' };
}
