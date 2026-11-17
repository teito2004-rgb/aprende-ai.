#!/usr/bin/env python3
"""Encaixa a locução real: mede as pausas, corta as cenas pela fala, gera som e projeto.

Uso (na pasta do projeto, com audio/locucao.mp3 presente):
    python3 tools/finalizar.py
Depois: npx hyperframes check && npx hyperframes render -q delivery -o renders/Nico-Explica-Palavra-Repetida.mp4
"""
import json, re, subprocess, sys, os

VOZ = "audio/locucao.mp3"
if not os.path.exists(VOZ):
    sys.exit("falta audio/locucao.mp3")

subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", VOZ, "-ac", "1", "-ar", "48000", "audio/locucao.wav"], check=True)
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", "audio/locucao.wav"]).decode())

# pausas (silêncio > 0,18 s abaixo de -38 dB)
log = subprocess.run(["ffmpeg", "-i", "audio/locucao.wav", "-af", "silencedetect=noise=-38dB:d=0.18", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
pausas = [((a + b) / 2, b - a) for a, b in zip(ini, fim)]
print(f"voz {dur:.2f}s, {len(pausas)} pausas")

cfg = json.load(open("cenas.json"))
cenas = cfg["cenas"]
cfg["duracao_voz"] = round(dur, 2)
# estimativa por caracteres -> pausa mais próxima (dentro de 2,5 s), em ordem
total_chars = sum(len(c["fala"]) for c in cenas)
acum, usado = 0, 0.0
cenas[0]["inicio"] = 0.0
for k, c in enumerate(cenas[1:], 1):
    acum += len(cenas[k - 1]["fala"])
    if "inicio_manual" in c:  # medido ouvindo/lendo as pausas: prevalece
        c["inicio"] = c["inicio_manual"]; usado = c["inicio"]; print(f"  {c['id']:12s} manual {c['inicio']:6.2f}"); continue
    alvo = dur * acum / total_chars
    cands = [p for p in pausas if p[0] > usado + 0.8 and abs(p[0] - alvo) < 2.5]
    if cands:
        t = min(cands, key=lambda p: abs(p[0] - alvo) - 0.5 * p[1])[0]
    else:
        t = alvo
    c["inicio"] = round(t, 2); usado = t
    print(f"  {c['id']:12s} alvo {alvo:6.2f} -> {t:6.2f}")
json.dump(cfg, open("cenas.json", "w"), ensure_ascii=False, indent=1)

# ---------- som (Natasha: fala primeiro, efeitos só em ação visível) ----------
T = {c["id"]: c["inicio"] for c in cenas}
ev = [
    {"t": 0.05, "som": "pop", "volume_db": -14, "cena": "convite"},
    {"t": T["convite"] + 0.55, "som": "encaixe", "volume_db": -14, "cena": "cadeira aparece"},
    {"t": T["estranha"] + 0.4, "som": "whoosh", "volume_db": -16, "cena": "letras se soltam"},
    {"t": T["nome"] + 0.35, "som": "ding", "nota": "A5", "volume_db": -15, "cena": "nome"},
    {"t": T["laboratorio"] + 0.2, "som": "papel", "volume_db": -18, "cena": "laboratorio"},
    {"t": T["cerebro"] + 0.5, "som": "blip", "nota": "E6", "volume_db": -17, "cena": "grafico"},
    {"t": T["hipotese"] + 0.9, "som": "clique", "volume_db": -16, "cena": "fio liga"},
    {"t": T["final"] + (cenas[-1].get("fim", dur + 1.2) - T["final"]) * 0.55 if False else T["final"] + 3.0, "som": "pop", "volume_db": -15, "cena": "balão"},
]
roteiro = {
    "duracao": round(dur + 1.2, 2), "bpm": 92, "semente": 26,
    "voz": "../audio/locucao.wav", "voz_ganho_db": 0,
    "cama": {"estilo": "curiosa", "tonica": "C3", "inicio": 0, "fim": round(dur + 1.0, 2), "volume_db": -8, "entrada": 1.0, "saida": 1.5},
    "ducking_db": -12, "alvo_lufs": -16, "teto_dbtp": -1.5, "eventos": ev,
}
os.makedirs("som/saida", exist_ok=True)
json.dump(roteiro, open("som/roteiro-som.json", "w"), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, "som_codigo.py", "roteiro-som.json", "saida"], cwd="som", check=True)
subprocess.run(["cp", "som/saida/mix.wav", "audio/mix.wav"], check=True)
print(open("som/saida/medicao.json").read())
subprocess.run([sys.executable, "tools/gerar.py"], check=True)
