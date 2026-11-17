#!/usr/bin/env python3
"""som_codigo.py — trilha, efeitos e mixagem gerados por código.

Uso:
    python som_codigo.py roteiro-som.json pasta-de-saida

Gera em pasta-de-saida/: efeitos.wav, cama.wav, mix.wav, cue-sheet.json, medicao.json.
Tudo determinístico (semente fixa): o mesmo roteiro gera sempre o mesmo som.
Dependências: numpy, scipy, pyloudnorm (pip install --break-system-packages pyloudnorm).
"""
import json, sys, os, wave
import numpy as np
from scipy.signal import butter, sosfilt, resample_poly
from scipy.ndimage import minimum_filter1d, uniform_filter1d

SR = 48000

# ---------------------------------------------------------------- utilidades
def db(x):
    return 10 ** (x / 20)

def filtro(x, tipo, f, ordem=2):
    f = np.clip(np.atleast_1d(f), 20, SR / 2 - 100)
    sos = butter(ordem, f if len(f) > 1 else f[0], btype=tipo, fs=SR, output="sos")
    return sosfilt(sos, x)

def env(n, ataque, decaimento):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(ataque, 1e-4)) * np.exp(-t / max(decaimento, 1e-4))

def ruido(rng, n):
    return rng.standard_normal(n)

def nota(nome):
    """'A4' -> 440 Hz. Aceita também número em Hz."""
    if isinstance(nome, (int, float)):
        return float(nome)
    nomes = {"C": -9, "C#": -8, "D": -7, "D#": -6, "E": -5, "F": -4, "F#": -3,
             "G": -2, "G#": -1, "A": 0, "A#": 1, "B": 2}
    letra, oit = nome[:-1], int(nome[-1])
    return 440.0 * 2 ** ((nomes[letra] + 12 * (oit - 4)) / 12)

# ---------------------------------------------------------------- efeitos
def s_whoosh(rng, dur=0.6, reverso=False, **_):
    n = int(dur * SR); x = np.linspace(0, 1, n); s = ruido(rng, n)
    corte = 400 + 3000 * np.sin(np.pi * x) ** 2
    s = filtro(s, "bandpass", [300, 5000]) * 0.6 + filtro(s, "lowpass", 900) * 0.6
    e = np.sin(np.pi * x) ** 2 if not reverso else x ** 3
    return s * e * (0.6 + 0.4 * corte / corte.max())

def s_riser(rng, dur=1.5, **_):
    n = int(dur * SR); x = np.linspace(0, 1, n)
    s = filtro(ruido(rng, n), "highpass", 400) * x ** 2.5 * 0.5
    f = 200 + 2200 * x ** 2
    s += 0.25 * np.sin(2 * np.pi * np.cumsum(f) / SR) * x ** 2
    return s

def s_impacto(rng, dur=1.2, **_):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 32 + 230 * np.exp(-t * 28)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.45)
    s += filtro(ruido(rng, n), "lowpass", 2500) * env(n, 0.001, 0.3) * 0.6
    return np.tanh(s * 1.5)

def s_sub_drop(rng, dur=1.0, **_):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 90 * np.exp(-t * 2.2) + 30
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.01, dur / 2)

def s_blip(rng, nota_="E6", dur=0.25, **_):
    f = nota(nota_); n = int(dur * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * f * t + 1.5 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t * 25)) * env(n, 0.002, 0.07)

def s_pop(rng, dur=0.15, **_):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 900 * np.exp(-t * 40) + 250
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.001, 0.035)

def s_clique(rng, dur=0.05, **_):
    n = int(dur * SR)
    return filtro(ruido(rng, n), "bandpass", [2000, 8000]) * env(n, 0.0005, 0.006) * 1.5

def s_encaixe(rng, dur=0.25, **_):
    a = s_clique(rng); b = s_pop(rng) * 0.8
    n = int(dur * SR); t = np.arange(n) / SR
    c = np.sin(2 * np.pi * 110 * t) * env(n, 0.001, 0.05) * 0.7
    out = np.zeros(n); out[:len(a)] += a; out[:len(b)] += b; out += c
    return out

def s_papel(rng, dur=0.5, **_):
    n = int(dur * SR); out = np.zeros(n)
    for _ in range(int(dur * 40)):
        i = rng.integers(0, n - 2000); m = rng.integers(300, 1800)
        g = rng.uniform(0.2, 1.0)
        out[i:i + m] += filtro(ruido(rng, m), "bandpass", [1500, 7000]) * env(m, 0.001, m / SR / 3) * g
    return out * np.sin(np.pi * np.linspace(0, 1, n)) ** 0.5

def s_ding(rng, nota_="A5", dur=1.5, **_):
    f = nota(nota_); n = int(dur * SR); t = np.arange(n) / SR
    parciais = [(1, 1.0, 1.2), (2.76, 0.5, 0.6), (5.4, 0.25, 0.3), (8.93, 0.12, 0.2)]
    return sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / d) for r, a, d in parciais) * env(n, 0.002, 10) * 0.6

def s_acerto(rng, dur=0.6, **_):
    n = int(dur * SR); out = np.zeros(n)
    for k, nm in enumerate(["C6", "G6"]):
        b = s_ding(rng, nm, dur=0.5); i = int(k * 0.09 * SR)
        out[i:i + len(b)] += b[:n - i]
    return out

def s_erro(rng, dur=0.35, **_):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.sign(np.sin(2 * np.pi * 110 * t)) * 0.4 + np.sign(np.sin(2 * np.pi * 116 * t)) * 0.4
    return filtro(s, "lowpass", 1800) * env(n, 0.005, 0.25)

def s_tique(rng, dur=0.08, **_):
    n = int(dur * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 2400 * t) * 0.5 + filtro(ruido(rng, n), "highpass", 3000) * 0.5) * env(n, 0.0005, 0.01)

def s_bolha(rng, dur=0.18, **_):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 300 + 1400 * (t / dur) ** 1.5
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.003, 0.06)

def s_digitar(rng, dur=1.0, **_):
    n = int(dur * SR); out = np.zeros(n); i = 0
    while i < n - 3000:
        c = s_clique(rng) * rng.uniform(0.5, 1.0)
        out[i:i + len(c)] += c; i += int(rng.uniform(0.06, 0.14) * SR)
    return out

EFEITOS = {
    "whoosh": s_whoosh, "riser": s_riser, "impacto": s_impacto, "sub_drop": s_sub_drop,
    "blip": s_blip, "pop": s_pop, "clique": s_clique, "encaixe": s_encaixe, "papel": s_papel,
    "ding": s_ding, "acerto": s_acerto, "erro": s_erro, "tique": s_tique, "bolha": s_bolha,
    "digitar": s_digitar,
}

# ---------------------------------------------------------------- cama musical
PROGRESSOES = {  # graus em semitons a partir da tônica
    "curiosa": [[0, 4, 7], [9, 12, 16], [5, 9, 12], [7, 11, 14]],     # I vi IV V (maior)
    "leve":    [[0, 4, 7, 11], [5, 9, 12, 16], [9, 12, 16], [7, 11, 14]],
    "tensa":   [[0, 3, 7], [8, 12, 15], [5, 8, 12], [7, 10, 14]],     # i VI iv v (menor)
    "misterio":[[0, 3, 7], [1, 5, 8], [0, 3, 7], [-1, 3, 6]],
}

def cama(rng, dur, bpm, estilo, tonica="C3"):
    n = int(dur * SR); t = np.arange(n) / SR
    out = np.zeros((n, 2))
    if estilo == "nenhuma":
        return out
    prog = PROGRESSOES.get(estilo, PROGRESSOES["curiosa"])
    f0 = nota(tonica); compasso = 4 * 60 / bpm
    # pad suave
    pad = np.zeros(n)
    for i in range(int(np.ceil(dur / compasso))):
        a, b = int(i * compasso * SR), min(n, int((i + 1) * compasso * SR))
        tt = t[a:b] - t[a]
        for st in prog[i % len(prog)]:
            f = f0 * 2 ** (st / 12)
            for det in (-0.4, 0.4):
                pad[a:b] += np.sin(2 * np.pi * f * (1 + det / 100) * tt + st)
        pad[a:b] *= np.minimum(1, tt / 0.3) * np.minimum(1, (tt[-1] - tt + 1e-3) / 0.3)
    pad = filtro(pad, "lowpass", 1400) * 0.08
    # arpejo dedilhado (pluck) a cada colcheia
    arp = np.zeros(n); passo = 60 / bpm / 2
    for k in range(int(dur / passo)):
        acorde = prog[int(k * passo / compasso) % len(prog)]
        st = acorde[k % len(acorde)] + 12
        f = f0 * 2 ** (st / 12); m = int(0.5 * SR); i = int(k * passo * SR)
        if i + m > n: break
        tt = np.arange(m) / SR
        arp[i:i + m] += (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(4 * np.pi * f * tt)) * env(m, 0.003, 0.18) * (0.9 if k % 4 == 0 else 0.6)
    arp *= 0.07
    # pulso leve (bumbo macio só nas cabeças de tempo, se tensa/curiosa)
    perc = np.zeros(n)
    if estilo in ("curiosa", "tensa"):
        for k in range(int(dur * bpm / 60)):
            i = int(k * 60 / bpm * SR); m = int(0.3 * SR)
            if i + m > n: break
            tt = np.arange(m) / SR; f = 45 + 80 * np.exp(-tt * 35)
            perc[i:i + m] += np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.12) * (0.18 if k % 4 == 0 else 0.1)
    lfo = 0.5 + 0.5 * np.sin(2 * np.pi * 0.07 * t)
    out[:, 0] = pad * (0.8 + 0.2 * lfo) + arp * 0.9 + perc
    out[:, 1] = pad * (1.0 - 0.2 * lfo) + arp * 1.1 + perc
    return out

# ---------------------------------------------------------------- mixagem
def ler_wav(caminho):
    import subprocess
    tmp = caminho + ".48k.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", caminho, "-ar", str(SR), "-ac", "2", "-sample_fmt", "s16", tmp], check=True)
    with wave.open(tmp) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, 2) / 32768.0
    os.remove(tmp)
    return x

def gravar_wav(caminho, x):
    x = np.clip(x, -1, 1)
    with wave.open(caminho, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())

def envelope_voz(voz, n, reducao_db, ataque=0.05, soltura=0.35):
    """Ganho de ducking: 1 sem voz, db(reducao_db) com voz."""
    mono = np.abs(voz.mean(1))[:n]
    mono = np.pad(mono, (0, max(0, n - len(mono))))
    janela = int(0.03 * SR)
    rms = np.sqrt(uniform_filter1d(mono ** 2, janela))
    limiar = max(1e-4, np.percentile(rms[rms > 0], 60) * 0.25) if np.any(rms > 0) else 1
    alvo = np.where(rms > limiar, db(reducao_db), 1.0)
    g = np.empty(n); atual = 1.0
    a_coef = np.exp(-1 / (ataque * SR)); s_coef = np.exp(-1 / (soltura * SR))
    for i in range(0, n, 64):  # passo de 64 amostras basta
        c = a_coef ** 64 if alvo[i] < atual else s_coef ** 64
        atual = c * atual + (1 - c) * alvo[i]
        g[i:i + 64] = atual
    return g

def pico_real_db(x):
    sobre = resample_poly(x, 4, 1, axis=0)
    return 20 * np.log10(np.max(np.abs(sobre)) + 1e-12)

def limitador(x, teto_db):
    teto = db(teto_db)
    pico = np.max(np.abs(x), axis=1)
    ganho = np.minimum(1, teto / np.maximum(pico, 1e-9))
    ganho = minimum_filter1d(ganho, int(0.005 * SR))
    ganho = uniform_filter1d(ganho, int(0.005 * SR))
    return x * ganho[:, None]

def medir_lufs(x):
    import pyloudnorm as pyln
    return pyln.Meter(SR).integrated_loudness(x)

# ---------------------------------------------------------------- principal
def principal(roteiro_path, saida):
    r = json.load(open(roteiro_path, encoding="utf-8"))
    os.makedirs(saida, exist_ok=True)
    rng = np.random.default_rng(r.get("semente", 7))
    dur = float(r["duracao"]); n = int(dur * SR)
    base = os.path.dirname(os.path.abspath(roteiro_path))

    # efeitos
    fx = np.zeros((n, 2)); cue = []
    for ev in r.get("eventos", []):
        nome = ev["som"]
        if nome not in EFEITOS:
            raise SystemExit(f"som desconhecido: {nome}. Opções: {', '.join(EFEITOS)}")
        kw = {k: v for k, v in ev.items() if k in ("dur", "reverso")}
        if "nota" in ev: kw["nota_"] = ev["nota"]
        s = EFEITOS[nome](rng, **kw) * db(ev.get("volume_db", -12))
        pan = float(ev.get("pan", 0)); l, rr = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        i = int(float(ev["t"]) * SR); m = min(len(s), n - i)
        if m <= 0: continue
        fx[i:i + m, 0] += s[:m] * l * 1.414; fx[i:i + m, 1] += s[:m] * rr * 1.414
        cue.append({"t": ev["t"], "som": nome, "cena": ev.get("cena", ""), "origem": "sintetizado por código (som_codigo.py)"})

    # cama
    c = r.get("cama", {"estilo": "nenhuma"})
    musica = cama(rng, dur, float(r.get("bpm", 96)), c.get("estilo", "curiosa"), c.get("tonica", "C3"))
    ini, fim = float(c.get("inicio", 0)), float(c.get("fim", dur))
    t = np.arange(n) / SR
    mascara = np.clip((t - ini) / max(0.01, c.get("entrada", 1.0)), 0, 1) * np.clip((fim - t) / max(0.01, c.get("saida", 1.5)), 0, 1)
    musica *= mascara[:, None] * db(c.get("volume_db", -6))
    if c.get("estilo", "nenhuma") != "nenhuma":
        cue.append({"t": ini, "som": f"cama musical ({c.get('estilo')}, {r.get('bpm', 96)} BPM)", "origem": "sintetizado por código (som_codigo.py)"})

    # voz e ducking
    voz = np.zeros((n, 2))
    if r.get("voz"):
        v = ler_wav(os.path.join(base, r["voz"])) * db(r.get("voz_ganho_db", 0))
        voz[:min(n, len(v))] = v[:n]
        g = envelope_voz(voz, n, float(r.get("ducking_db", -10)))
        musica *= g[:, None]
        fx *= (0.5 + 0.5 * g)[:, None]  # efeitos abaixam menos que a música

    gravar_wav(os.path.join(saida, "efeitos.wav"), fx)
    gravar_wav(os.path.join(saida, "cama.wav"), musica)

    # master: soma, loudness alvo, teto de pico
    mix = voz + musica + fx
    alvo, teto = float(r.get("alvo_lufs", -16)), float(r.get("teto_dbtp", -1.5))
    lufs0 = medir_lufs(mix)
    mix *= db(alvo - lufs0)
    for _ in range(3):
        if pico_real_db(mix) <= teto: break
        mix = limitador(mix, teto - 0.3)
        mix *= db(alvo - medir_lufs(mix))
    mix = limitador(mix, teto - 0.3)
    excesso = pico_real_db(mix) - teto
    if excesso > 0:  # pico entre amostras: baixa só o necessário
        mix *= db(-(excesso + 0.05))
    f = int(0.02 * SR); mix[-f:] *= np.linspace(1, 0, f)[:, None]
    gravar_wav(os.path.join(saida, "mix.wav"), mix)

    med = {"duracao_s": dur, "lufs_integrado": round(medir_lufs(mix), 2), "pico_real_dbtp": round(pico_real_db(mix), 2),
           "alvo_lufs": alvo, "teto_dbtp": teto, "eventos": len(cue)}
    json.dump(cue, open(os.path.join(saida, "cue-sheet.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump(med, open(os.path.join(saida, "medicao.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(med, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    principal(sys.argv[1], sys.argv[2])
