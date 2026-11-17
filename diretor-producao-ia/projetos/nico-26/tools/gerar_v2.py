#!/usr/bin/env python3
"""Nico Explica #26 — v2 no padrão visual dos episódios de melhor desempenho.

Padrão (análise vidIQ de Tesla, Bocejo e Atenção, 17/11/2026):
título no alto à esquerda · ilustração vetorial grande no centro (contorno carvão grosso,
preenchimento creme/branco, detalhes ciano) · nota pequena abaixo · legenda em pílula
carvão com texto claro, 2–4 palavras · fundo alternando amarelo/creme · cena nova a cada
~3–4 s · elementos de app (like, enquete, comentário).
Tempos das frases medidos nas pausas da locução (audio/locucao.wav).
"""
import json, os, html, shutil

W, H = 1080, 1920
AM, CR, CA, CI, BR = "#FFDC44", "#FFF9E9", "#171B18", "#27CDE0", "#FFFFFF"
DUR_VOZ = 58.88
TOTAL = 60.1

# ---------------- frases medidas (início, fim, texto) ----------------
FRASES = [
    (0.00, 0.68, "Faz comigo:"),
    (1.11, 4.22, "repete em voz alta, sem parar, uma palavra bem comum."),
    (4.68, 5.88, "Pode ser cadeira."),
    (6.30, 6.56, "Vai:"),
    (7.05, 13.32, "cadeira, cadeira, cadeira, cadeira, cadeira, cadeira, cadeira, cadeira, cadeira, cadeira."),
    (13.45, 13.96, "Ficou estranha?"),
    (14.49, 15.22, "Parece só um som?"),
    (15.54, 16.49, "Se aconteceu com você,"),
    (16.97, 19.95, "deixa um like pra eu saber que funcionou."),
    (20.44, 21.15, "Isso tem nome:"),
    (21.43, 22.97, "saciedade semântica."),
    (23.43, 24.24, "Em laboratório,"),
    (24.40, 27.15, "depois de ver o nome de uma categoria"),
    (27.35, 28.20, "umas trinta vezes,"),
    (28.40, 31.47, "em vez de três, as pessoas demoram mais pra dizer se uma palavra pertence a ela,"),
    (31.70, 33.47, "tipo se maçã é uma fruta."),
    (33.90, 35.62, "E, em estudos com eletrodos,"),
    (35.79, 39.50, "a resposta do cérebro ligada ao significado ficou mais fraca"),
    (39.64, 41.71, "depois de trinta repetições do que depois de três."),
    (42.17, 42.83, "Uma hipótese:"),
    (43.23, 44.24, "de tanto repetir,"),
    (44.42, 46.27, "a ligação entre o som e o sentido"),
    (46.41, 47.36, "cansa por um momento."),
    (47.84, 50.76, "Onde exatamente isso acontece ainda está em debate."),
    (51.20, 52.14, "Se não sentiu nada,"),
    (52.33, 52.72, "tudo bem:"),
    (53.08, 56.17, "o efeito não aparece pra todo mundo, nem em todo teste."),
    (56.67, 58.66, "Qual palavra ficou mais estranha pra você?"),
]

def chunks(a, b, txt, maxw=3):
    ws = txt.split(); out = []; cur = []
    for w in ws:
        cur.append(w)
        if len(cur) >= maxw or w.endswith((",", ".", "?", ":")):
            out.append(" ".join(cur)); cur = []
    if cur: out.append(" ".join(cur))
    tot = sum(len(c) for c in out); t = a; res = []
    for c in out:
        d = (b - a) * len(c) / tot
        res.append([c, round(t, 2), round(t + d, 2)]); t += d
    # cobre a pausa seguinte com a última pílula (sem piscar)
    return res

LEG = []
for i, (a, b, t) in enumerate(FRASES):
    if t.startswith("cadeira, cadeira"):
        n = 10; d = (b - a) / n
        LEG += [["cadeira", round(a + k * d, 2), round(a + (k + 1) * d, 2)] for k in range(n)]
    else:
        LEG += chunks(a, b, t)
# estende cada pílula até a próxima (máx +0,5 s) para não piscar
for k in range(len(LEG) - 1):
    LEG[k][2] = round(min(LEG[k + 1][1], LEG[k][2] + 0.5), 2)

# ---------------- peças de ilustração ----------------
def svg(w, h, body, vb=None, extra=""):
    return f'<svg width="{w}" height="{h}" viewBox="{vb or f"0 0 {w} {h}"}" fill="none" stroke="{CA}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round" {extra}>{body}</svg>'

def cadeira(fill):
    return svg(360, 440, f'''
<rect x="70" y="20" width="220" height="200" rx="18" fill="{fill}"/>
<rect x="110" y="60" width="140" height="18" rx="9" fill="{CI}" stroke="none"/>
<rect x="40" y="220" width="280" height="56" rx="14" fill="{fill}"/>
<path d="M70 276 V420 M290 276 V420"/>''')

def cartao(txt, fill, size=96, w=760, h=220, extra=""):
    return f'<div class="card" style="width:{w}px;height:{h}px;background:{fill};font-size:{size}px" {extra}>{html.escape(txt)}</div>'

def like(prefix):
    return f'''<div class="like" id="{prefix}-like"><div class="like-c"><svg width="60" height="60" viewBox="0 0 24 24" fill="{CA}"><path d="M2 21h4V9H2v12zm20-11a2 2 0 0 0-2-2h-6.3l1-4.6v-.3c0-.4-.2-.8-.4-1.1L13.2 1 6.6 7.6C6.2 8 6 8.5 6 9v10a2 2 0 0 0 2 2h9c.8 0 1.5-.5 1.8-1.2l3-7.1c.1-.2.2-.5.2-.7v-2z"/></svg></div><div class="like-p">deixa um like</div></div>'''

# ---------------- cenas ----------------
CENAS = []
def cena(id, t, cor, titulo, corpo, anim="", nota="", css=""):
    CENAS.append(dict(id=id, t=t, cor=cor, titulo=titulo, corpo=corpo, anim=anim, nota=nota, css=css))

E = lambda sel, t, y=36, d=0.4: f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:{d},ease:"power3.out"}},{t});\n'
POP = lambda sel, t: f'tl.fromTo("{sel}",{{opacity:0,scale:0.85}},{{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"}},{t});\n'

# 1 gancho
cena("gancho", 0.0, AM, "Faz comigo:<br>repete em voz alta",
     f'<div class="ilu" id="g-ilu">{cadeira(CR)}</div>',
     POP("#g-ilu", 0.15), nota="uma palavra bem comum")
# 2 a palavra
cena("palavra", 4.55, CR, "Pode ser<br>“cadeira”.",
     f'<div class="ilu" id="p-card">{cartao("cadeira", BR, 120)}</div>',
     POP("#p-card", 0.1) + 'tl.fromTo("#p-card .card",{boxShadow:"0px 0px 0 #171B18"},{boxShadow:"14px 14px 0 #171B18",duration:0.4},0.4);\n',
     nota="Vai, junto comigo.")
# 3 repetição com contador
cont = "".join(f'<div class="num" id="n{k}">×{k+1}</div>' for k in range(10))
pilha = "".join(f'<div class="mini" id="m{k}" style="left:{(k%2)*380}px;top:{(k//2)*86}px">cadeira</div>' for k in range(10))
an = ""
for k in range(10):
    t0 = round(7.05 - 6.85 + k * 0.627, 2)
    an += f'tl.fromTo("#m{k}",{{opacity:0,y:20}},{{opacity:{round(1-k*0.07,2)},y:0,duration:0.25}},{t0});\n'
    an += f'tl.fromTo("#n{k}",{{opacity:0}},{{opacity:1,duration:0.05}},{t0});\n'
    if k < 9: an += f'tl.to("#n{k}",{{opacity:0,duration:0.05}},{round(t0+0.6,2)});\n'
cena("repeticao", 6.85, AM, "Repete<br>10 vezes",
     f'<div id="r-cont">{cont}</div><div id="r-pilha">{pilha}</div><div id="r-bar-bg"></div><div id="r-bar"></div>',
     an + 'tl.fromTo("#r-bar",{scaleX:0},{scaleX:1,duration:6.3,ease:"none"},0.2);\n',
     css=f"""#r-cont{{position:absolute;right:170px;top:300px;width:260px;height:150px}}
.num{{position:absolute;right:0;top:0;font-size:120px;font-weight:900;color:{CA}}}
#r-pilha{{position:absolute;left:150px;top:520px;width:780px;height:440px}}
.mini{{position:absolute;width:360px;height:70px;border:6px solid {CA};border-radius:16px;background:{CR};font-size:44px;font-weight:800;display:flex;align-items:center;justify-content:center}}
#r-bar-bg{{position:absolute;left:150px;right:150px;top:1010px;height:18px;border-radius:9px;background:{CA}33}}
#r-bar{{position:absolute;left:150px;top:1010px;width:780px;height:18px;border-radius:9px;background:{CI};transform-origin:left center}}""")
# 4 ficou estranha
letras = "".join(f'<span class="lt" id="lt{k}">{c}</span>' for k, c in enumerate("cadeira"))
barras = "".join(f'<div class="br" id="br{k}" style="left:{k*58}px"></div>' for k in range(13))
rots = [-16, 10, -7, 18, -11, 8, -14]; ys = [24, -34, 28, -18, 34, -28, 12]; hs = [70,140,200,100,220,160,80,180,120,210,90,150,60]
an = POP("#e-card", 0.05)
for k in range(7): an += f'tl.fromTo("#lt{k}",{{rotation:0,y:0}},{{rotation:{rots[k]},y:{ys[k]},duration:0.8,ease:"power2.inOut"}},{0.3+k*0.05});\n'
for k in range(13): an += f'tl.fromTo("#br{k}",{{height:12}},{{height:{hs[k]},duration:0.4,ease:"power2.out"}},{0.9+k*0.03});\n'
cena("estranha", 13.4, CR, "Ficou estranha?<br>Virou só som?",
     f'<div class="ilu" id="e-card" data-layout-allow-overlap><div class="card" style="width:760px;height:220px;background:{BR};font-size:120px">{letras}</div></div><div id="e-onda">{barras}</div>',
     an, css=f""".lt{{display:inline-block}} #e-onda{{position:absolute;left:170px;top:880px;width:760px;height:230px}}
.br{{position:absolute;bottom:0;width:34px;border-radius:17px;background:{CA}}}""")
# 5 enquete + like
cena("enquete", 15.4, AM, "Aconteceu<br>com você?",
     f'''<div id="q-box"><div class="opt" id="q1"><span class="dot"></span>virou só som</div><div class="opt" id="q2"><span class="dot"></span>continuou normal</div></div>{like("q")}''',
     E("#q1", 0.2) + E("#q2", 0.35) + 'tl.fromTo("#q1 .dot",{backgroundColor:"#FFFFFF"},{backgroundColor:"#27CDE0",duration:0.2},1.2);\n' + POP("#q-like", 1.6),
     css=f"""#q-box{{position:absolute;left:150px;right:150px;top:560px;display:flex;flex-direction:column;gap:34px}}
.opt{{height:130px;border:8px solid {CA};border-radius:65px;background:{CR};font-size:54px;font-weight:800;display:flex;align-items:center;gap:30px;padding:0 44px}}
.dot{{width:50px;height:50px;border-radius:25px;border:7px solid {CA};background:#fff}}
#q-like{{position:absolute;left:0;right:0;top:960px}}""")
# 6 nome
cena("nome", 20.3, CR, "Isso tem nome",
     f'<div class="ilu" id="nm-card">{cartao("saciedade semântica", BR, 76, 840, 240)}</div>',
     POP("#nm-card", 1.15), nota="Termo de L. Jakobovits James, 1962")
# 7 laboratório: tela FRUTA ×30
cena("laboratorio", 23.3, AM, "Em laboratório",
     f'''<div class="ilu" id="lb-tela">{svg(720, 520, f'<rect x="10" y="10" width="700" height="420" rx="30" fill="{CR}"/><path d="M300 430 L280 500 H440 L420 430" fill="{CR}"/>')}</div>
<div id="lb-pal">FRUTA</div><div id="lb-x3" class="badge">×3</div><div id="lb-x30" class="badge" style="background:{CI}">×30</div>''',
     POP("#lb-tela", 0.1) + E("#lb-pal", 0.5) + POP("#lb-x3", 1.4) + 'tl.to("#lb-x3",{opacity:0,duration:0.2},3.9);\n' + POP("#lb-x30", 4.05),
     nota="o nome de uma categoria, repetido",
     css=f"""#lb-pal{{position:absolute;left:0;right:0;top:640px;text-align:center;font-size:110px;font-weight:900;letter-spacing:.04em}}
.badge{{position:absolute;right:130px;top:470px;padding:14px 34px;border-radius:50px;background:{CR};border:7px solid {CA};font-size:64px;font-weight:900}}""")
# 8 maçã é fruta? cronômetros
cena("tempo", 28.3, CR, "“maçã” é<br>uma fruta?",
     f'''<div id="tp-box"><div class="tp-l">depois de 3×</div><div class="tp-b" id="tp-1"></div><div class="tp-l">depois de 30×</div><div class="tp-b" id="tp-2" style="background:{CI}"></div></div><div id="tp-r">resposta mais lenta</div>''',
     E("#tp-box", 0.1) + 'tl.fromTo("#tp-1",{width:0},{width:330,duration:0.7,ease:"power2.out"},0.6);\n' + 'tl.fromTo("#tp-2",{width:0},{width:640,duration:1.6,ease:"power2.out"},1.6);\n' + POP("#tp-r", 3.4),
     nota="Smith &amp; Klein, 1990 · tempo ilustrativo",
     css=f"""#tp-box{{position:absolute;left:150px;right:150px;top:540px;display:flex;flex-direction:column;gap:18px}}
.tp-l{{font-size:44px;font-weight:800}} .tp-b{{height:74px;border:7px solid {CA};border-radius:20px;background:{BR}}}
#tp-r{{position:absolute;left:150px;top:900px;padding:16px 34px;border-radius:50px;background:{CA};color:{CR};font-size:46px;font-weight:800}}""")
# 9 eletrodos
el = "".join(f'<circle cx="{x}" cy="{y}" r="22" fill="{CI}"/>' for x, y in [(250,120),(360,80),(470,120),(200,220),(520,220),(300,180),(420,180)])
cena("eletrodos", 33.75, AM, "Estudos com<br>eletrodos",
     f'<div class="ilu" id="el-ilu">{svg(720, 520, f"<path d=\'M150 470 C40 300 120 40 360 40 C600 40 680 300 570 470 Z\' fill=\'{CR}\'/>" + el + f"<path d=\'M570 300 C680 320 680 420 640 470\'/>")}</div>',
     POP("#el-ilu", 0.1), nota="sinal do cérebro")
# 10 gráfico
import math
def onda(amp):
    return " ".join(f"{x},{(-amp*math.exp(-((x-390)/95)**2)):.1f}" for x in range(0, 781, 10))
cena("sinal", 35.7, CR, "Sinal do<br>significado",
     f'''<svg id="sg-g" style="position:absolute;left:150px;top:560px" width="780" height="420" viewBox="0 -300 780 420">
<line x1="0" y1="0" x2="780" y2="0" stroke="{CA}" stroke-opacity=".3" stroke-width="4"/>
<polyline id="sg-a" points="{onda(260)}" stroke="{CA}" stroke-width="12" fill="none" stroke-linecap="round"/>
<polyline id="sg-b" points="{onda(115)}" stroke="{CI}" stroke-width="12" fill="none" stroke-linecap="round"/></svg>
<div id="sg-l"><span class="pl" style="background:{CA};color:{CR}">3×</span> <span class="pl" style="background:{CI}">30× mais fraco</span></div>''',
     'tl.fromTo("#sg-a",{opacity:0},{opacity:1,duration:0.5},0.2);\n' + 'tl.fromTo("#sg-b",{opacity:0},{opacity:1,duration:0.5},2.6);\n' + E("#sg-l", 2.7),
     nota="Kounios et al., 2000 · Ströberg et al., 2017 · esquema",
     css=f"""#sg-l{{position:absolute;left:150px;top:880px;display:flex;gap:16px}} .pl{{padding:12px 28px;border-radius:40px;font-size:40px;font-weight:800}}""")
# 11 hipótese som ↔ sentido
cena("hipotese", 41.95, AM, "Uma hipótese",
     f'''<div class="tag" id="hp-tag">hipótese</div><div class="box" id="hp-a" style="left:140px">som</div><div class="box" id="hp-b" style="left:610px">sentido</div><div id="hp-fio"></div>''',
     E("#hp-tag", 0.1, 20) + POP("#hp-a", 0.3) + POP("#hp-b", 0.45) + 'tl.fromTo("#hp-fio",{scaleX:0},{scaleX:1,duration:0.5},0.7);\n',
     nota="de tanto repetir…",
     css=f""".tag{{position:absolute;left:150px;top:470px;padding:10px 28px;border-radius:40px;border:6px solid {CA};font-size:40px;font-weight:800;background:{CR}}}
.box{{position:absolute;top:640px;width:280px;height:200px;border:9px solid {CA};border-radius:28px;background:{CR};display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:900}}
#hp-fio{{position:absolute;left:420px;top:722px;width:190px;height:36px;border-radius:18px;background:{CA};transform-origin:left center}}""")
# 12 a ligação cansa
cena("cansa", 45.2, CR, "A ligação cansa<br>por um momento",
     f'''<div class="box" id="cs-a" style="left:140px">som</div><div class="box" id="cs-b" style="left:610px">sentido</div><div id="cs-fio"></div>''',
     'tl.fromTo("#cs-fio",{scaleY:1,opacity:1},{scaleY:0.15,opacity:0.35,duration:1.4,ease:"power1.inOut"},1.0);\n',
     css=f""".box{{position:absolute;top:640px;width:280px;height:200px;border:9px solid {CA};border-radius:28px;background:{BR};display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:900}}
#cs-fio{{position:absolute;left:420px;top:722px;width:190px;height:36px;border-radius:18px;background:{CA}}}""")
# 13 em debate
cena("debate", 47.6, AM, "Onde acontece?<br>Ainda em debate",
     f'<div class="ilu" id="db-ilu">{svg(520, 520, f"<circle cx=\'220\' cy=\'220\' r=\'170\' fill=\'{CR}\'/><path d=\'M345 345 L480 480\' stroke-width=\'34\'/><text x=\'220\' y=\'285\' text-anchor=\'middle\' font-size=\'200\' font-weight=\'900\' fill=\'{CA}\' stroke=\'none\' font-family=\'Inter\'>?</text>")}</div>',
     POP("#db-ilu", 0.15) + 'tl.fromTo("#db-ilu",{rotation:-6},{rotation:6,duration:1.4,ease:"sine.inOut"},0.6);\n',
     nota="percepção ou significado? os estudos divergem")
# 14 não sentiu
cena("tudobem", 51.0, CR, "Não sentiu nada?<br>Tudo bem.",
     f'''<div id="tb-box"><div class="tb" id="tb1">nem todo mundo sente</div><div class="tb" id="tb2">nem todo teste mostra</div></div>''',
     E("#tb1", 1.6) + E("#tb2", 3.2),
     css=f"""#tb-box{{position:absolute;left:150px;right:150px;top:600px;display:flex;flex-direction:column;gap:34px}}
.tb{{height:140px;border:8px solid {CA};border-radius:30px;background:{BR};font-size:52px;font-weight:800;display:flex;align-items:center;padding:0 44px}}""")
# 15 comentário
cena("comentario", 56.4, AM, "Qual palavra<br>ficou estranha?",
     f'''<div id="cm-card"><div class="cm-top"><span class="av"></span><b>você</b></div><div class="cm-in" id="cm-in">banana, banana, banana…</div></div>
<div id="cm-chips"><span class="chip">cadeira</span><span class="chip">janela</span><span class="chip">ovo</span></div>''',
     POP("#cm-card", 0.1) + E("#cm-chips", 0.6),
     nota="conta nos comentários",
     css=f"""#cm-card{{position:absolute;left:150px;right:150px;top:560px;padding:36px;border:8px solid {CA};border-radius:34px;background:{CR}}}
.cm-top{{display:flex;align-items:center;gap:20px;font-size:40px;margin-bottom:24px}} .av{{width:70px;height:70px;border-radius:35px;background:{CI};border:6px solid {CA}}}
.cm-in{{font-size:50px;font-weight:700;border-bottom:6px solid {CA};padding-bottom:12px}}
#cm-chips{{position:absolute;left:150px;top:900px;display:flex;gap:18px}} .chip{{padding:12px 30px;border-radius:40px;background:{CA};color:{CR};font-size:40px;font-weight:800}}""")

# ---------------- escrita ----------------
BASE = f"""#root{{position:absolute;inset:0;overflow:hidden;font-family:Inter,sans-serif;color:{CA}}}
.bg{{position:absolute;inset:0}}
.tit{{position:absolute;left:120px;right:160px;top:300px;font-size:84px;font-weight:900;line-height:1.05;letter-spacing:-0.025em}}
.ilu{{position:absolute;left:0;right:0;top:500px;height:520px;display:flex;align-items:center;justify-content:center}}
.card{{border:9px solid {CA};border-radius:34px;display:flex;align-items:center;justify-content:center;font-weight:900;letter-spacing:-0.01em;text-align:center;line-height:1.05}}
.nota{{position:absolute;left:150px;right:200px;top:1050px;text-align:center;font-size:32px;font-weight:500;opacity:.8}}
.like{{display:flex;align-items:center;justify-content:center;gap:22px}}
.like-c{{width:120px;height:120px;border-radius:60px;background:{CI};border:7px solid {CA};display:flex;align-items:center;justify-content:center}}
.like-p{{padding:20px 40px;border-radius:60px;border:7px solid {CA};background:#fff;font-size:48px;font-weight:800}}"""

os.makedirs("compositions", exist_ok=True)
for f in os.listdir("compositions"):
    if f.endswith(".html"): os.remove(os.path.join("compositions", f))
for i, c in enumerate(CENAS):
    fim = CENAS[i + 1]["t"] if i + 1 < len(CENAS) else TOTAL
    c["dur"] = round(fim - c["t"], 2)
    nota = f'<div class="nota" id="{c["id"]}-nota">{c["nota"]}</div>' if c["nota"] else ""
    an = E(f'#{c["id"]}-tit', 0.0, 24, 0.3) + c["anim"] + (E(f'#{c["id"]}-nota', 0.5, 12) if c["nota"] else "")
    open(f'compositions/{c["id"]}.html', "w").write(f"""<template>
<style>{BASE}
{c['css']}</style>
<div id="root" data-composition-id="{c['id']}" data-width="{W}" data-height="{H}">
<div class="bg" style="background:{c['cor']}"></div>
<div class="tit" id="{c['id']}-tit">{c['titulo']}</div>
{c['corpo']}
{nota}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{an}tl.to({{}}, {{ duration: {c['dur']} }}, 0);
window.__timelines["{c['id']}"] = tl;
</script>
</template>
""")

items = "\n".join(f'<div id="lg{k}" class="clip lg" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="1"><span>{html.escape(t)}</span></div>' for k, (t, a, b) in enumerate(LEG))
open("compositions/legendas.html", "w").write(f"""<template>
<style>#root{{position:absolute;inset:0;font-family:Inter,sans-serif}}
.lg{{position:absolute;left:150px;right:190px;top:1150px;text-align:center}}
.lg span{{display:inline-block;padding:12px 26px;border-radius:16px;background:{CA};color:{CR};font-size:46px;font-weight:700;line-height:1.15}}</style>
<div id="root" data-composition-id="legendas" data-width="{W}" data-height="{H}" data-layout-allow-caption-zone>
{items}
</div>
<script>const tl = gsap.timeline({{ paused: true }}); tl.to({{}}, {{ duration: {TOTAL} }}, 0); window.__timelines["legendas"] = tl;</script>
</template>
""")

hosts = "\n".join(f'<div id="{c["id"]}" data-composition-id="{c["id"]}" data-composition-src="compositions/{c["id"]}.html" data-start="{c["t"]}" data-duration="{c["dur"]}" data-track-index="1" data-track-kind="graphics" data-width="{W}" data-height="{H}"></div>' for c in CENAS)
shutil.copy("audio/mix.wav", "assets/mix.wav")
open("index.html", "w").write(f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="UTF-8" /><meta name="viewport" content="width={W}, height={H}" />
<script src="assets/vendor/gsap.min.js"></script>
<style>*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{AM}}}</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}" data-fps="30">
{hosts}
<div id="legendas" data-composition-id="legendas" data-composition-src="compositions/legendas.html" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-track-kind="captions" data-width="{W}" data-height="{H}"></div>
<audio id="trilha" class="clip" src="assets/mix.wav" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-volume="1"></audio>
</div>
<script>window.__timelines["main"] = gsap.timeline({{ paused: true }});</script>
</body></html>
""")

def ts(x):
    return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int(round((x-int(x))*1000)):03d}"
with open("legendas.srt", "w") as f:
    for k, (t, a, b) in enumerate(LEG, 1): f.write(f"{k}\n{ts(a)} --> {ts(b)}\n{t}\n\n")
print("v2:", len(CENAS), "cenas,", len(LEG), "legendas")
