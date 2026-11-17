#!/usr/bin/env python3
"""Gera o projeto HyperFrames do Nico Explica #26 a partir de cenas.json.

Tempos: se cenas.json tiver "inicio" em cada cena (medido na locução), usa;
senão distribui a duração da voz pelo tamanho da fala (estimativa provisória).
Uso: python3 tools/gerar.py   (rodar na pasta do projeto)
"""
import json, os, re, html

W, H, FPS = 1080, 1920, 30
C = {"amarelo": "#FFDC44", "creme": "#FFF9E9", "carvao": "#171B18", "ciano": "#27CDE0"}
CAUDA = 1.2  # respiro depois da última fala

cfg = json.load(open("cenas.json"))
cenas = cfg["cenas"]
dur_voz = cfg["duracao_voz"]

# ---------- tempos ----------
if all("inicio" in c for c in cenas):
    for i, c in enumerate(cenas):
        c["fim"] = cenas[i + 1]["inicio"] if i + 1 < len(cenas) else dur_voz + CAUDA
    estimado = False
else:
    pesos = [len(c["fala"]) for c in cenas]
    t = 0.0
    for c, p in zip(cenas, pesos):
        c["inicio"] = round(t, 2)
        t += dur_voz * p / sum(pesos)
        c["fim"] = round(t, 2)
    cenas[-1]["fim"] = round(dur_voz + CAUDA, 2)
    estimado = True
TOTAL = round(cenas[-1]["fim"], 2)

# ---------- legendas: blocos de até ~6 palavras, tempo pelo tamanho ----------
def blocos(texto, max_pal=4):
    pal = texto.split()
    out, cur = [], []
    for w in pal:
        cur.append(w)
        if len(cur) >= max_pal or re.search(r"[.?!:]$", w):
            out.append(" ".join(cur)); cur = []
    if cur: out.append(" ".join(cur))
    return out

legendas = []
for c in cenas:
    fim_fala = min(c["fim"], dur_voz) if c is cenas[-1] else c["fim"]
    if "falas" in c:  # tempos de palavra medidos (lista [texto, ini, fim])
        legendas += c["falas"]; continue
    bs = blocos(c["fala"]); tot = sum(len(b) for b in bs); t = c["inicio"]
    for b in bs:
        d = (fim_fala - c["inicio"]) * len(b) / tot
        legendas.append([b, round(t, 2), round(t + d, 2)]); t += d

# ---------- cenas ----------
BASE_CSS = f"""
#root {{ position:absolute; inset:0; overflow:hidden; font-family:Inter, sans-serif; color:{C['carvao']}; }}
.bg {{ position:absolute; inset:0; }}
.titulo {{ position:absolute; left:120px; right:180px; font-weight:800; font-size:78px; line-height:1.08; letter-spacing:-0.02em; }}
.nota {{ position:absolute; left:120px; right:180px; font-size:29px; font-weight:500; opacity:.75; }}
"""

def cena_html(c, corpo, anim, extra_css=""):
    cid = c["id"]; dur = round(c["fim"] - c["inicio"], 2)
    return f"""<template>
<style>{BASE_CSS}{extra_css}</style>
<div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
  <div class="bg" style="background:{C[c['cor']]}"></div>
  {corpo}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{anim}
tl.to({{}}, {{ duration: {dur} }}, 0);
window.__timelines["{cid}"] = tl;
</script>
</template>
"""

def entra(sel, t, y=40, d=0.45):
    return f'tl.fromTo("{sel}", {{opacity:0, y:{y}}}, {{opacity:1, y:0, duration:{d}, ease:"power3.out"}}, {t});\n'

CADEIRA_SVG = f"""<svg viewBox="0 0 200 260" width="300" height="390" fill="none" stroke="{C['carvao']}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round">
<path d="M50 20 V140 H150 V20"/><path d="M50 60 H150"/><path d="M40 140 H160"/><path d="M55 140 V245"/><path d="M145 140 V245"/></svg>"""

def build(c):
    i, d = c["id"], c["fim"] - c["inicio"]
    if i == "convite":
        corpo = f"""<div id="cv-t" class="titulo" style="top:330px">Faz comigo:<br>repete em voz alta</div>
<div id="cv-ic" style="position:absolute;left:390px;top:560px">{CADEIRA_SVG}</div>
<div id="cv-w" class="titulo" style="top:960px;font-size:120px;text-align:center;left:120px;right:120px">cadeira</div>"""
        anim = entra("#cv-t", 0.0) + entra("#cv-ic", 0.5) + entra("#cv-w", min(1.2, d * 0.5))
        return cena_html(c, corpo, anim)
    if i == "repeticao":
        linhas = "".join(f'<div class="rp" id="rp{k}" style="top:{330 + k*72}px">cadeira</div>' for k in range(10))
        corpo = f"""{linhas}<div id="rp-bar-bg" style="position:absolute;left:120px;right:180px;top:1090px;height:14px;border-radius:7px;background:{C['carvao']}22"></div>
<div id="rp-bar" style="position:absolute;left:120px;top:1090px;height:14px;width:780px;border-radius:7px;background:{C['ciano']};transform-origin:left center"></div>"""
        css = ".rp{position:absolute;left:140px;font-weight:800;font-size:62px;letter-spacing:-.01em}"
        anim = ""
        for k in range(10):
            t = round(d * k / 10, 2)
            alvo = round(1 - k * 0.075, 2)
            anim += f'tl.fromTo("#rp{k}", {{opacity:0, x:-30}}, {{opacity:{alvo}, x:0, duration:0.3, ease:"power2.out"}}, {t});\n'
        anim += f'tl.fromTo("#rp-bar", {{scaleX:0}}, {{scaleX:1, duration:{round(d,2)}, ease:"none"}}, 0);\n'
        return cena_html(c, corpo, anim, css)
    if i == "estranha":
        letras = "".join(f'<span class="lt" id="lt{k}">{ch}</span>' for k, ch in enumerate("cadeira"))
        barras = "".join(f'<div class="br" id="br{k}" style="left:{140 + k*52}px"></div>' for k in range(14))
        corpo = f"""<div id="es-t" class="titulo" style="top:330px">Ficou estranha?<br>Virou só som?</div>
<div id="es-l" data-layout-allow-overlap style="position:absolute;left:120px;right:120px;top:560px;text-align:center;font-weight:800;font-size:130px">{letras}</div>
<div style="position:absolute;left:0;top:820px;width:100%;height:220px">{barras}</div>
<div id="es-like" class="titulo" style="top:1050px;font-size:50px;right:120px">👍 Funcionou? Deixa um like</div>"""
        css = f".lt{{display:inline-block}} .br{{position:absolute;bottom:0;width:30px;border-radius:15px;background:{C['carvao']}}}"
        anim = entra("#es-t", 0)
        rots = [-14, 9, -6, 16, -10, 7, -12]; ys = [20, -30, 25, -15, 30, -25, 10]
        for k in range(7):
            anim += f'tl.fromTo("#lt{k}", {{rotation:0, y:0}}, {{rotation:{rots[k]}, y:{ys[k]}, duration:0.9, ease:"power2.inOut"}}, {0.4 + k*0.06});\n'
        hs = [60, 120, 180, 90, 200, 140, 70, 160, 110, 190, 80, 150, 100, 60]
        for k in range(14):
            anim += f'tl.fromTo("#br{k}", {{height:10}}, {{height:{hs[k]}, duration:0.5, ease:"power2.out"}}, {0.6 + k*0.04});\n'
        anim += entra("#es-like", round(d * 0.45, 2))
        return cena_html(c, corpo, anim, css)
    if i == "nome":
        corpo = f"""<div id="nm-e" class="nota" style="top:560px">Isso tem nome:</div>
<div id="nm-t" class="titulo" style="top:630px;font-size:104px">Saciedade<br>semântica</div>
<div id="nm-l" style="position:absolute;left:120px;top:900px;width:260px;height:12px;border-radius:6px;background:{C['ciano']};transform-origin:left center"></div>
<div id="nm-n" class="nota" style="top:1040px">Termo de L. Jakobovits James (1962)</div>"""
        anim = entra("#nm-e", 0) + entra("#nm-t", 0.35) + 'tl.fromTo("#nm-l",{scaleX:0},{scaleX:1,duration:0.6,ease:"power3.out"},0.8);\n' + entra("#nm-n", 0.5, 20)
        return cena_html(c, corpo, anim)
    if i == "laboratorio":
        corpo = f"""<div id="lb-t" class="titulo" style="top:330px;font-size:66px">Ver o nome da categoria…</div>
<div id="lb-q" class="titulo" style="top:500px;font-size:52px;font-weight:700">“maçã” é uma fruta?</div>
<div class="lb-row" id="lb-r1" style="top:600px"><span class="lb-k">3 vezes</span><div class="lb-bar" id="lb-b1" style="width:300px;background:{C['carvao']}"></div></div>
<div class="lb-row" id="lb-r2" style="top:780px"><span class="lb-k">30 vezes</span><div class="lb-bar" id="lb-b2" style="width:520px;background:{C['carvao']}"></div></div>
<div id="lb-ax" class="nota" style="top:900px">tempo para responder (ilustrativo)</div>
<div id="lb-r" class="titulo" style="top:960px;font-size:60px">Resposta mais lenta</div>
<div id="lb-f" class="nota" style="top:1050px">Smith &amp; Klein (1990)</div>"""
        css = ".lb-row{position:absolute;left:120px;right:120px;height:120px}.lb-k{display:block;font-size:40px;font-weight:700;margin-bottom:10px}.lb-bar{height:56px;border-radius:12px;transform-origin:left center}"
        anim = (entra("#lb-t", 0) + entra("#lb-q", round(d*0.55,2)) + entra("#lb-r1", round(d*0.15,2)) +
                f'tl.fromTo("#lb-b1",{{scaleX:0}},{{scaleX:1,duration:0.8,ease:"power2.out"}},{round(d*0.15+0.2,2)});\n' +
                entra("#lb-r2", round(d*0.35,2)) +
                f'tl.fromTo("#lb-b2",{{scaleX:0}},{{scaleX:1,duration:1.6,ease:"power2.out"}},{round(d*0.35+0.2,2)});\n' +
                entra("#lb-ax", round(d*0.4,2), 15) + entra("#lb-r", round(d*0.7,2)) + entra("#lb-f", round(d*0.72,2), 15))
        return cena_html(c, corpo, anim, css)
    if i == "cerebro":
        def onda(amp):
            pts = []
            for x in range(0, 781, 10):
                import math
                y = 0 if x < 200 else -amp * math.exp(-((x - 400) / 90) ** 2)
                pts.append(f"{x},{y:.1f}")
            return " ".join(pts)
        corpo = f"""<div id="cb-t" class="titulo" style="top:330px;font-size:66px">Sinal do significado</div>
<svg id="cb-g" style="position:absolute;left:120px;top:500px" width="780" height="460" viewBox="0 -300 780 460">
  <line x1="0" y1="0" x2="780" y2="0" stroke="{C['carvao']}" stroke-opacity=".25" stroke-width="3"/>
  <polyline id="cb-a" points="{onda(240)}" fill="none" stroke="{C['carvao']}" stroke-width="9" stroke-linecap="round"/>
  <polyline id="cb-b" points="{onda(110)}" fill="none" stroke="{C['ciano']}" stroke-width="9" stroke-linecap="round"/>
</svg>
<div id="cb-la" class="nota" style="top:960px;opacity:1;font-weight:700">— depois de 3 repetições</div>
<div id="cb-lb" class="nota" style="top:1000px;opacity:1;font-weight:700;color:#0d8fa0">— depois de 30: mais fraco</div>
<div id="cb-f" class="nota" style="top:1050px;font-size:26px">Kounios et al. (2000); Ströberg et al. (2017) · ilustrativo</div>"""
        anim = (entra("#cb-t", 0) + 'tl.fromTo("#cb-a",{opacity:0},{opacity:1,duration:0.6},0.5);\n' + entra("#cb-la", 0.6, 15) +
                f'tl.fromTo("#cb-b",{{opacity:0}},{{opacity:1,duration:0.6}},{round(d*0.5,2)});\n' + entra("#cb-lb", round(d*0.5,2), 15) + entra("#cb-f", round(d*0.55,2), 15))
        return cena_html(c, corpo, anim)
    if i == "hipotese":
        corpo = f"""<div id="hp-tag" style="position:absolute;left:120px;top:330px;padding:10px 24px;border:4px solid {C['carvao']};border-radius:40px;font-size:36px;font-weight:700">hipótese</div>
<div id="hp-a" class="hp-box" style="left:120px">som</div>
<div id="hp-b" class="hp-box" style="left:640px">sentido</div>
<div id="hp-fio" style="position:absolute;left:380px;top:735px;width:260px;height:26px;border-radius:13px;background:{C['carvao']}"></div>
<div id="hp-t" class="titulo" style="top:900px;font-size:62px">A ligação cansa<br>por um momento</div>
<div id="hp-n" class="nota" style="top:1070px">Onde isso acontece ainda está em debate</div>"""
        css = f".hp-box{{position:absolute;top:660px;width:260px;height:170px;border-radius:24px;background:{C['creme']};border:5px solid {C['carvao']};display:flex;align-items:center;justify-content:center;font-size:50px;font-weight:800}}"
        anim = (entra("#hp-tag", 0, 20) + entra("#hp-a", 0.3) + entra("#hp-b", 0.5) +
                'tl.fromTo("#hp-fio",{scaleX:0},{scaleX:1,duration:0.6,ease:"power2.out"},0.9);\n' +
                f'tl.fromTo("#hp-fio",{{scaleY:1,opacity:1}},{{scaleY:0.18,opacity:0.45,duration:2.4,ease:"power1.inOut"}},{round(d*0.25,2)});\n' +
                entra("#hp-t", round(d*0.3,2)) + entra("#hp-n", round(d*0.6,2), 15))
        return cena_html(c, corpo, anim, css)
    if i == "final":
        corpo = f"""<div id="fn-t" class="titulo" style="top:330px;font-size:64px">Não sentiu nada?<br>Tudo bem.</div>
<div id="fn-n" class="nota" style="top:510px;font-size:36px;opacity:.85">O efeito não aparece pra todo mundo, nem em todo teste.</div>
<div id="fn-b" style="position:absolute;left:120px;right:180px;top:700px;padding:44px 48px;background:{C['amarelo']};border-radius:36px;font-size:60px;font-weight:800;line-height:1.12">Qual palavra ficou mais estranha pra você?</div>
<div id="fn-r" style="position:absolute;left:190px;top:1010px;width:0;height:0;border-left:40px solid transparent;border-right:40px solid transparent;border-top:56px solid {C['amarelo']}"></div>
<div id="fn-c" class="nota" style="top:1060px;opacity:1;font-weight:700">💬 Conta nos comentários</div>"""
        anim = entra("#fn-t", 0) + entra("#fn-n", 0.5, 15) + entra("#fn-b", round(d*0.55,2)) + entra("#fn-r", round(d*0.55,2), 20) + entra("#fn-c", round(d*0.62,2), 15)
        return cena_html(c, corpo, anim)
    raise SystemExit("cena sem layout: " + i)

os.makedirs("compositions", exist_ok=True)
for c in cenas:
    open(f"compositions/{c['id']}.html", "w").write(build(c))

# ---------- legendas (uma composição) ----------
leg_items = "\n".join(
    f'  <div id="lg{k}" class="clip lg" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="1">{html.escape(t)}</div>'
    for k, (t, a, b) in enumerate(legendas))
leg = f"""<template>
<style>
#root {{ position:absolute; inset:0; font-family:Inter, sans-serif; }}
.lg {{ position:absolute; left:120px; right:220px; top:1140px; text-align:center; font-size:43px; font-weight:700; line-height:1.2; color:{C['carvao']}; background:{C['creme']}; border:3px solid {C['carvao']}; border-radius:18px; padding:14px 20px; }}
</style>
<div id="root" data-composition-id="legendas" data-width="{W}" data-height="{H}" data-layout-allow-caption-zone>
{leg_items}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
tl.to({{}}, {{ duration: {TOTAL} }}, 0);
window.__timelines["legendas"] = tl;
</script>
</template>
"""
open("compositions/legendas.html", "w").write(leg)

# ---------- index ----------
hosts = "\n".join(
    f'      <div id="{c["id"]}" data-composition-id="{c["id"]}" data-composition-src="compositions/{c["id"]}.html" '
    f'data-start="{c["inicio"]}" data-duration="{round(c["fim"]-c["inicio"],2)}" data-track-index="1" data-track-kind="graphics" '
    f'data-width="{W}" data-height="{H}"></div>' for c in cenas)
audio = ""
for nome in ("audio/mix.wav", "audio/locucao.mp3"):
    if os.path.exists(nome):
        audio = f'      <audio id="trilha" class="clip" src="{"assets/" + os.path.basename(nome)}" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-volume="1"></audio>'
        os.makedirs("assets", exist_ok=True)
        import shutil; shutil.copy(nome, "assets/" + os.path.basename(nome))
        break
index = f"""<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ width:{W}px; height:{H}px; overflow:hidden; background:{C['creme']}; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}" data-fps="{FPS}">
{hosts}
      <div id="legendas" data-composition-id="legendas" data-composition-src="compositions/legendas.html" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-track-kind="captions" data-width="{W}" data-height="{H}"></div>
{audio}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
open("index.html", "w").write(index)

# ---------- legendas.srt ----------
def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s-int(s))*1000)):03d}"
with open("legendas.srt", "w") as f:
    for k, (t, a, b) in enumerate(legendas, 1):
        f.write(f"{k}\n{ts(a)} --> {ts(b)}\n{t}\n\n")
json.dump({"estimado": estimado, "total": TOTAL, "cenas": [{k: c[k] for k in ("id", "inicio", "fim", "cor")} for c in cenas]},
          open("tempos.json", "w"), ensure_ascii=False, indent=1)
print("ok", "estimado" if estimado else "medido", TOTAL, "s,", len(legendas), "legendas, audio:", audio != "")
