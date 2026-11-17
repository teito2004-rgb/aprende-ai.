"""Inventario incremental de fontes locais (Markdown e DOCX).

Nao interpreta nem executa as fontes: so extrai texto, calcula hash,
guarda extratos e mantem a fila de revisao em 09-varreduras/.
"""
import argparse
import hashlib
import json
import os
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

DEFAULT_BRAIN = Path(os.environ.get('CEREBRO_DIR', 'Clayton cerebro'))
SKIP = {'node_modules', '.git', '.venv', 'venv', 'site-packages', 'python-packages',
        '__pycache__', '.cache', 'vendor', 'dist', 'build', 'models', 'checkpoints',
        'pydeps', 'ocr-deps', 'audio-libs', 'qwen-audio'}
KEEP_DOT = {'.agents', '.claude', '.codex'}
SECRET = re.compile(r'sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{25,}|ghp_[A-Za-z0-9]{25,}'
                    r'|hf_[A-Za-z0-9]{25,}|AIza[A-Za-z0-9_-]{30,}')
W_NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def atomic_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
    os.replace(temp, path)


def extract(path, raw):
    if path.suffix.lower() != '.docx':
        return raw.decode('utf-8-sig', errors='replace'), None
    chunks = []
    with zipfile.ZipFile(path) as archive:
        selected = [x for x in archive.infolist() if re.fullmatch(
            r'word/(document|header\d*|footer\d*|footnotes|endnotes|comments)\.xml', x.filename)]
        if sum(x.file_size for x in selected) > 32_000_000:
            raise ValueError('DOCX XML acima do limite de 32 MB')
        for item in selected:
            tree = ET.fromstring(archive.read(item))
            paragraphs = [''.join(t.text or '' for t in p.findall('.//w:t', W_NS))
                          for p in tree.findall('.//w:p', W_NS)]
            chunks.append('[' + item.filename + ']\n' + '\n'.join(paragraphs))
    return ('\n\n'.join(chunks),
            'Texto DOCX parcial: sem imagens/layout; revisoes podem requerer leitura especifica.')


def scan(roots, brain):
    brain = Path(brain).resolve()
    out = brain / '09-varreduras'
    state_path = out / 'estado-arquivos.json'
    state = (json.loads(state_path.read_text(encoding='utf-8'))
             if state_path.exists() else {'schema_version': 1, 'files': {}})
    if state.get('schema_version') != 1:
        raise ValueError('Versao de estado desconhecida; preservar arquivo e revisar')
    now = datetime.now(timezone.utc).isoformat()
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    errors, changed, seen, count = [], [], set(), 0
    for root in roots:
        root = Path(root).resolve()
        if not root.exists():
            errors.append({'source': str(root), 'error': 'raiz indisponivel'})
            continue

        def onerror(exc):
            errors.append({'source': str(exc.filename), 'error': type(exc).__name__})

        for here, dirs, names in os.walk(root, onerror=onerror, followlinks=False):
            here = Path(here)
            kept = []
            for d in dirs:
                if d.lower() in SKIP or (d.startswith('.') and d not in KEEP_DOT):
                    continue
                child = here / d
                try:
                    if child.is_symlink():
                        continue
                    if os.name == 'nt' and child.stat().st_file_attributes & 1024:
                        continue
                    if child.resolve() != brain:
                        kept.append(d)
                except OSError as exc:
                    errors.append({'source': str(child), 'error': type(exc).__name__})
            dirs[:] = kept
            if here == brain or brain in here.parents:
                dirs[:] = []
                continue
            for name in names:
                p = here / name
                if name.startswith(('~$', '.env')) or p.suffix.lower() not in {'.md', '.docx'}:
                    continue
                key = str(p)
                if key in seen:
                    continue
                seen.add(key)
                count += 1
                try:
                    if p.is_symlink():
                        continue
                    if p.stat().st_size > 8_000_000:
                        errors.append({'source': key, 'error': 'arquivo acima de 8 MB'})
                        continue
                    raw = p.read_bytes()
                    sha = hashlib.sha256(raw).hexdigest()
                    old = state['files'].get(key, {})
                    if old.get('observed_sha256') == sha:
                        old['last_seen'] = now
                        continue
                    text, limitation = extract(p, raw)
                    if SECRET.search(text):
                        errors.append({'source': key,
                                       'error': 'possivel credencial; extrato omitido'})
                        continue
                    docid = hashlib.sha256(key.encode('utf-8')).hexdigest()[:20]
                    rel = Path('extratos') / docid / (sha + '.md')
                    target = out / rel
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text('# Fonte para revisao\n\n' + key + '\nSHA-256: ' + sha
                                      + '\nObservado em: ' + now + '\n'
                                      + (limitation or '') + '\n\n' + text, encoding='utf-8')
                    entry = {'source': key, 'observed_sha256': sha,
                             'reviewed_sha256': old.get('reviewed_sha256'),
                             'excerpt': rel.as_posix(), 'last_seen': now,
                             'limitation': limitation}
                    for field in ('findings', 'last_reviewed'):
                        if field in old:
                            entry[field] = old[field]
                    state['files'][key] = entry
                    changed.append(key)
                except (OSError, ValueError, zipfile.BadZipFile, ET.ParseError) as exc:
                    errors.append({'source': key, 'error': type(exc).__name__})
    pending = [x['source'] for x in state['files'].values()
               if x.get('reviewed_sha256') != x.get('observed_sha256')]
    state['last_inventory_at'] = now
    state['last_roots'] = [str(x) for x in roots]
    atomic_json(state_path, state)
    report = {'at': now, 'roots': state['last_roots'], 'files_seen': count,
              'new_or_changed': changed, 'pending_review': pending, 'errors': errors,
              'note': 'Inventario local; sem leitura de chats nem revisao semantica. '
                      'Fontes ausentes nao sao apagadas.'}
    atomic_json(out / 'inventarios' / (stamp + '.json'), report)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', action='append', type=Path,
                        help='pasta de fontes (repetivel); padrao: pasta atual')
    parser.add_argument('--brain', type=Path, default=DEFAULT_BRAIN)
    args = parser.parse_args()
    result = scan(args.root or [Path('.')], args.brain)
    print(json.dumps({'files_seen': result['files_seen'],
                      'new_or_changed': len(result['new_or_changed']),
                      'pending_review': len(result['pending_review']),
                      'errors': len(result['errors'])}))
