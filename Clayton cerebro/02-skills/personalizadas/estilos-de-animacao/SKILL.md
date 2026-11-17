---
name: "estilos-de-animacao"
description: "Animar qualquer tema em 17 estilos (pixel art, quadro-negro, neon, PS2, quadrinhos, vetorial, 3D, blocos de montar, massinha, recorte de papel, anime anos 90, cartaz antigo, maquete, low poly, isométrico, 3D de objetos, traço técnico) no HyperFrames, vertical 9:16."
---

# Estilos de animação

Catálogo de 17 estilos prontos para Reels/Shorts (1080×1920, 30 fps), feitos no HyperFrames. Sempre carregue `/hyperframes` antes de construir: o contrato dele (clip, data-start, timeline pausada, nada de aleatório sem semente) vale aqui.

## Como trabalhar

1. Descobrir: qual estilo (ou mistura), qual tema/personagem, duração. Sem resposta: 1 estilo, ~8 s, personagem original.
2. Projeto: `npx hyperframes init <pasta> --skip-skills --skill=hyperframes`; trocar o viewport para 1080×1920.
3. **Bibliotecas e fontes locais** (o CDN pode ser bloqueado no render):
   - `npm pack gsap@3.15.0 three@0.160.0` → copiar `gsap.min.js` e `three.min.js` para `assets/lib/` e apontar o `<script>` do index para lá.
   - Fontes: `npm pack @fontsource/<nome>` → copiar o `.woff2` latin para `assets/fonts/` e declarar `@font-face` dentro da cena.
4. Uma cena por arquivo em `compositions/`, id do host = id da cena = chave da timeline.
5. Layout vertical: texto entre y 168 e 1330; título ~y 250, "estilo N de 13" (ou N de quantos entrarem no vídeo) ~y 430, personagem no meio (caixa ~540×720 em left 270, top 610).
6. `npx hyperframes check --json` → `snapshot --at ...` → olhar a folha de contatos → corrigir → `render -o arquivo.mp4`.
7. Nunca copiar personagem ou marca conhecida (nada de Mario, Pokémon etc.): criar um personagem original.

## Os 17 estilos

### 1. Pixel art (8-bit)
- Canvas de baixa resolução (ex.: 108×192) ampliado 10× com `image-rendering: pixelated`. Desenhar uma vez no init (céu em faixas com dithering, sol listrado, montanhas, chão em tile de 16 px).
- Paleta estilo PICO-8: #1d2b53 #7e2553 #ff004d #ffa300 #ffec27 #fff1e8 #29adff #008751 #ab5236.
- Fonte: Press Start 2P, sombra dura (`text-shadow: 10px 10px 0`).
- Movimento **sempre em degraus**: `ease: "steps(n)"`. Sprite de corrida = 2 quadros alternados com `tl.set` a cada 0,125 s. Chão rola com `repeat` finito.
- Extras: moedas com `scaleX` em degraus (giro), "+1", HUD "MOEDAS x0" (um span por número, trocados por clip).

### 2. Quadro-negro
- Fundo #233a2f com manchas radiais claras (giz apagado) e moldura de madeira (#7a5230, borda 34 px).
- Traços SVG com `pathLength="1"`, `stroke-dasharray:1`, animar `strokeDashoffset` 1→0 parte por parte (~0,3 s cada, defasado 0,1 s): parece desenhado na hora.
- Filtro de giz: `feTurbulence` (fractalNoise, baseFrequency 0.8, seed fixa) + `feDisplacementMap` scale 4.
- Fonte: Caveat 700. Anotação amarela (#f7d76b) com seta desenhada e texto revelado por `clip-path: inset()`.

### 3. Desenho que brilha (neon)
- Fundo quase preto com vinheta roxa (#1b0b2e → #06050b).
- Traço claro (#bff9ff / #ffd0f4 / #fff6b0) + `drop-shadow` empilhado na cor do tubo (ciano #2ef2ff, rosa #ff3ec8, amarelo #ffe94a).
- Desenha com dashoffset e depois **falha**: `tl.set` de opacidade 1→0,3→1 em poucos quadros (tubo piscando). Título com `text-shadow` em 4 camadas.

### 4. Estilo PS2 (low-poly)
- three.js renderizando em 216×384 e ampliado com pixelated; `flatShading`, `MeshLambertMaterial`, antialias desligado.
- Neblina azul (#0a1a50), chão xadrez em textura 8×8 com NearestFilter, cristais translúcidos flutuando (vibe de tela de boot).
- "Tremidinha" da época: arredondar posições de câmera/objeto a uma grade (`Math.round(v/0.08)*0.08`).
- Título cromado: Montserrat 900 itálico com gradiente prata recortado no texto; scanlines com `repeating-linear-gradient`; "CARREGANDO..." piscando.
- Câmera a ~9 unidades, começando pela frente do personagem.

### 5. Quadrinhos
- Fundo amarelo #ffd23f com retícula (`radial-gradient` em pontos de 24 px).
- Painel com borda preta de 14 px, linhas de ação radiais, personagem com contorno preto 7 px, cores chapadas e sombra em retícula (`<pattern>` de pontos).
- Fonte: Bangers, com `-webkit-text-stroke` + sombra dura, levemente rotacionada.
- Balão "OI, GALERA!" e explosão "POW!" entrando com `back.out(2.5–3)`, mais um soquinho de escala no personagem.

### 6. Ilustração vetorial (flat)
- Fundo creme #f6efe3, formas grandes chapadas (#ffb703, #8ecae6, #219ebc, #fb8500, #023047), sem contorno.
- Fonte: Poppins 700 alinhada à esquerda. Texto pequeno colorido precisa de contraste (laranja escuro #c96a00 sobre creme).
- Movimento macio: entrada `back.out(1.7)`, formas flutuando com `sine.inOut` yoyo finito, piscada (`scaleY` 0,1) e aceno.

### 7. 3D
- three.js em resolução cheia, `MeshStandardMaterial`, ACES tone mapping, sombras PCF suaves.
- Luz: key quente (#ffd9b0) com sombra, rim frio (#6fa8ff), hemisférica fraca; fundo #121419 com neblina; chão em disco escuro.
- Formas arredondadas (esferas, cápsulas), visor preto brilhante, olhos emissivos. Visor de esfera parcial virado para frente: `phiStart = π·0.18`, `phiLength = π·0.64`.
- Câmera a ~11,5 unidades, `lookAt` na altura do peito, giro lento + personagem girando e acenando.

### 8. Blocos de montar
- Nunca usar a marca ou o logo de nenhum fabricante: o nome no vídeo é "blocos de montar".
- Fundo = placa de base: cor chapada (#1e5bb8 céu, #2e8b3a chão) com grade de pinos (`radial-gradient` circular de 40 px com brilho no canto superior esquerdo e sombra embaixo).
- Tudo montado em retângulos de proporção de tijolo (múltiplos de 40 px), cores primárias saturadas (#d01012 #f5cd2f #0d69ab #237841 #ffffff), cantos levemente arredondados (4 px) e bevel com `box-shadow: inset`.
- Personagem original: cabeça cilíndrica amarela, mãos em C, corpo trapezoidal. Nuvens e árvores também em tijolos.
- Movimento: peças entram caindo e encaixam (`bounce.out` curto ou `steps(3)` no último trecho) com um "tec" de escala 1→0,96→1. Animação do personagem em poses fixas trocadas com `tl.set` (sensação de stop-motion, ~12 qps).
- Fonte: Fredoka 700 com contorno grosso.

### 9. Massinha (claymation)
- Formas orgânicas arredondadas, cores pastel saturadas (#ff6f59 #ffd166 #6cc4a1 #4d96ff #f7f1e3), sem contorno.
- Textura de massa: `feTurbulence` (baseFrequency ~0.9, seed fixa) + `feDiffuseLighting` sutil por cima de cada forma; marcas de dedo com 2–3 elipses levemente mais escuras.
- Sombra de contato macia sob cada objeto (elipse borrada) e luz vinda de cima.
- Movimento em "dois": animar a 12 qps (`steps` ou `tl.set` a cada 1/12 s) e trocar a seed do ruído a cada pose (seeds pré-definidas, nunca aleatórias) para o "ferver" típico do stop-motion. Squash & stretch nos pulos.
- Fonte: Baloo 2 800, com leve deformação via `scaleX/scaleY` alternados.

### 10. Recorte de papel
- Camadas de papel chapado (céu #8ecae6, nuvens #ffffff, montanhas #90be6d, chão #43aa8b) com borda levemente irregular (`feTurbulence` + `feDisplacementMap` scale 2–3) e textura de fibra (ruído fraco com `mix-blend-mode: multiply`).
- Cada camada com sombra projetada curta (`drop-shadow(0 6px 4px rgba(0,0,0,.25))`) para separar os planos.
- Personagem articulado em partes (tronco, braços, pernas, cabeça) girando em torno de "alfinetes" (`transform-origin` nas juntas), como marionete de papel.
- Movimento: parallax entre camadas, partes balançando com `sine.inOut`, entradas deslizando como se fossem empurradas à mão. Opcional: 15 qps para cara artesanal.
- Fonte: Patrick Hand ou Amatic SC 700, sobre etiqueta de papel recortado.

### 11. Anime anos 90
- Visual de animação em acetato (cel): personagem original com contorno fino escuro, cores chapadas e **uma** faixa de sombra dura (sem gradiente) + brilho de rim branco nos cabelos.
- Céu pintado à mão: gradiente azul (#3a7bd5 → #a8d8ff), nuvens grandes e volumosas com bordas suaves e sombra lilás (#c8b6e2).
- Filme da época: grão leve, leve desfoque de cor (aberração cromática de 1–2 px), vinheta suave e cores um pouco lavadas (`filter: saturate(.9) contrast(.95)`).
- Movimento "em três": 8 qps no personagem, fundo panorâmico deslizando liso; linhas de velocidade e brilho em estrela nos momentos de impacto.
- Fonte: M PLUS Rounded 1c 800 ou Zen Maru Gothic, legenda amarela com contorno preto.
- Não imitar personagens nem séries reais: só a linguagem visual.

### 12. Cartaz antigo (risografia)
- Fundo papel #f2ece0 com fibras. Só 2–3 cores de tinta: rosa fluorescente #ff48b0, azul #0078bf, amarelo #ffe800, misturando por `mix-blend-mode: multiply`.
- Cada cor em uma camada própria com **desalinhamento de registro** de 3–6 px entre elas.
- Granulado de impressão: retícula/ruído forte (`feTurbulence` alta frequência + `feComponentTransfer` com limiar) aplicado como máscara em cada camada, deixando falhas de tinta.
- Movimento: a 8–12 qps, trocando a seed do grão a cada quadro (seeds fixas) para o "chiado" de impressão; o registro das cores treme 1–2 px.
- Fonte: Archivo Black ou Bebas Neue, grande, na mesma tinta das camadas.

### 13. Maquete (diorama)
- A cena inteira vira um objeto físico: caixa/base de feltro verde sobre mesa de madeira (#8b5a2b com veios), fundo de parede desfocado.
- Cenário em papelão pintado e algodão (nuvens presas em arame), árvores de esponja; luz quente lateral com sombras de contato.
- Profundidade de campo rasa (efeito tilt-shift): faixa central nítida, `filter: blur()` crescente no topo e na base, saturação um pouco alta.
- Personagem como boneco de massa ou feltro preso por haste; movimento em stop-motion (12 qps) e câmera fazendo um leve dolly lateral (parallax entre base, mesa e parede).
- Pode ser em three.js (`DepthOfField` não é necessário: simular com camadas + blur) ou só em camadas CSS.
- Fonte: Fraunces 700 em uma plaquinha de papel na frente da maquete.

### 14. Low poly
- Diferente do PS2: resolução cheia, sem pixelado nem tremidinha, visual limpo e moderno.
- three.js com `flatShading: true` e `MeshLambertMaterial` (ou Standard com roughness 1): cada face com uma cor só. Geometrias com poucos segmentos (`IcosahedronGeometry` detail 0–1, cilindros de 5–7 lados, cones para árvores). Deformar vértices com ruído de seed fixa para relevo de montanhas e pedras.
- Paleta pastel quente (#f4a261 #e9c46a #2a9d8f #264653 #e76f51) e céu em gradiente CSS atrás do canvas (renderer com `alpha: true`).
- Luz direcional forte de lado + hemisférica suave para as faces ficarem bem diferentes entre si; neblina leve na cor do horizonte.
- Personagem original montado com sólidos facetados. Movimento macio (`sine.inOut`, `back.out`), câmera em órbita lenta.
- Fonte: Montserrat 800 ou Space Grotesk 700.

### 15. Isométrico
- Câmera ortográfica: three.js `OrthographicCamera` em posição (d, d, d) olhando para a origem (ângulo isométrico clássico: 35,264° de elevação, 45° de giro). Sem perspectiva: linhas paralelas continuam paralelas.
- Alternativa só em CSS/SVG: plano com `transform: rotateX(60deg) rotateZ(45deg)` ou desenho em grade isométrica (losangos 2:1).
- Cenário como "ilha" ou bloco cortado flutuando no fundo liso (#eef2f7 ou gradiente suave), com chão em tiles e laterais do bloco mais escuras (3 tons por cor: topo claro, esquerda médio, direita escuro).
- Paleta viva e chapada (#5e60ce #48bfe3 #72efdd #ffd166 #ef476f), sombras simples projetadas em diagonal.
- Movimento: objetos sobem do chão em sequência (`back.out(1.6)` no eixo y), personagem anda pela grade em linhas retas nos dois eixos isométricos, câmera fixa ou girando em degraus de 90°.
- Fonte: Poppins 700 ou Space Grotesk 700, texto reto (não isométrico) na faixa segura.

### 16. 3D de objetos (explicativo)
- Formato de curiosidade narrada: **um objeto-símbolo por frase** (calendário, cadeado, poltronas, celular com post, digital, avião de papel), sem personagem. Corte seco a cada 1–2 frases.
- Fundo escuro de estúdio: `radial-gradient(ellipse 70% 45% at 50% 42%, #262a33, #16181d 55%, #0e0f12)` atrás do canvas (`alpha: true`). Chão #17191e com disco #22252c (raio ~2,2) sob o objeto. Cenário só sugerido e apagado ao fundo (linhas de gráfico verde/vermelho a ~55% de opacidade, janelas, pista com luzinhas).
- Cor: objetos brancos/cinza-claro (`MeshPhysicalMaterial` #f3f4f6, roughness .32, clearcoat .6) e metal claro (#dfe2e7, metalness .55). **Uma única cor de destaque**, laranja #ff6a10, em uma parte de cada objeto. Pode ter 2–3 pontinhos laranja flutuando.
- Formas arredondadas: `RoundedBoxGeometry` e `RoomEnvironment` de `examples/jsm` (copiar para `assets/lib/` e trocar `from 'three'` pelo caminho local).
- Luz: ACES tone mapping, environment do RoomEnvironment (PMREM, sigma 0.04), key quente #fff1e0 (2,2) com sombra PCF suave, rim frio #9db8ff (1,4), hemisférica fraca; neblina #14161b de 20 a 40.
- Enquadramento testado (1080×1920): `PerspectiveCamera(28)`, posição (3,4, 5,6, 21), `lookAt(0, 1,25, 0)`, objeto com ~2,3 unidades de largura, leve giro (`rotation.y ≈ -0,38`). Objeto ocupa ~40% da largura, entre y ~580 e 1140.
- Legenda palavra por palavra: Inter 800 60 px, branco #f2f3f5 em caixa rgba(20,22,27,.88) com raio 22 px, centralizada em y ~1420; a palavra-chave em laranja. Trocar o texto por clip a cada palavra/bloco falado (tempo vindo da transcrição da narração).
- @ da página no topo (Inter 600 30 px, y ~250) com bolinha laranja antes.
- Movimento: objeto entra subindo/escalando com `back.out(1.6)`, depois giro lento em y (~15° em 2 s) e uma leve flutuação; câmera com dolly in de 3–5%. Final: "Compartilha **no story**" com avião de papel.

### 17. Traço técnico com anotações (line art)
- Formato de explicação narrada: um desenho-símbolo por frase (nuvem, poste, mapa, celular, avião de papel), centralizado no terço de cima, com muito espaço vazio. Referência: perfil Ilustrando Curiosidades (reel sobre tornados em SC, nov/2026).
- Fundo quase preto liso (#121212), sem textura. Só contorno: SVG com `stroke` branco (#EDEDED) de 1,5–2 px, `fill:none`, `stroke-linecap:round`. Nada de brilho, glow ou degradê (diferença para o neon, nº 3).
- Desenho aparece sendo traçado: `pathLength="1"` + `strokeDashoffset` 1→0 parte por parte (0,4–0,8 s cada), como no quadro-negro, mas linha limpa.
- Volume e sombra por **hachura**: linhas horizontais paralelas a cada 6–8 px, recortadas pela forma (`clipPath`), surgindo de cima para baixo.
- Cor com função: laranja (#FF7A2F) = perigo/destaque (raio, faísca, região do mapa); azul (#5BA8E0) = frio/água. Um ponto laranja pulsando por cena como marcador.
- **Anotações técnicas:** rótulo em fonte monoespaçada maiúscula (JetBrains Mono ou Space Mono 600, 22–26 px, laranja), ligado ao desenho por linha de chamada fina (1 px, 50% de opacidade) com ponto na ponta. Texto aparece letra a letra (`steps`) depois da linha.
- Legenda palavra por palavra **sem caixa**: Poppins/Inter 600, 46–52 px; palavra falada em branco 800, o resto em cinza (#8A8A8A). Fica logo abaixo do desenho, dentro da faixa segura.
- @ da página pequeno no topo (cinza, 22 px).
- Movimento: entre cenas, corte seco ou o desenho se apaga com dashoffset invertido; dentro da cena, só traçar, pulsar o ponto e pequenos deslocamentos (setas de vento, chuva em linhas). Câmera parada.
- Versão Nico: fundo creme #FFF9E9, linha carvão #171B18, destaques ciano #27CDE0 e amarelo #F5C531, anotações em carvão; legenda segue a regra do Nico (palavra-chave com marca-texto ciano).
- É o estilo mais leve para renderizar (só SVG, sem three.js): bom para episódios longos de 1–2 min.

## three.js no HyperFrames (PS2, 3D, low poly, isométrico e 3D de objetos)

Dirigir o render pela timeline, nunca por requestAnimationFrame:

```js
const st = { t: 0 };
tl.fromTo(st, { t: 0 }, { t: DUR, duration: DUR, ease: "none", onUpdate: () => render(st.t) }, 0);
render(0);
```

`render(t)` calcula tudo só a partir de `t`. Renderer com `preserveDrawingBuffer: true`. O aviso de "three.min.js deprecated" no check é inofensivo.

## Vídeo-vitrine (todos os estilos)

Mesmo personagem em todos, ~3 s por estilo, corte seco, título + "estilo N de X" em cada cena (X = quantos estilos entram no vídeo), final "QUAL É O SEU FAVORITO? / COMENTA O NÚMERO" listando os nomes cada um na fonte do seu estilo. Quadro 0 já mostra o primeiro estilo com título (nunca tela preta). Acima de ~15 s, oferecer trilha e efeitos (`/media-use`).

## Armadilhas já vistas

- Câmera 3D perto demais corta o personagem e bate no título: afastar e baixar o enquadramento antes de renderizar.
- Sprite pequeno some no vertical: personagem de pixel art com ~240 px de altura.
- Texto informativo dentro da faixa segura; nada importante embaixo de y 1330.
- `fromTo` sempre (não `from`), repetições finitas, aleatoriedade com semente.
- Estilos de stop-motion (massinha, blocos, recorte, maquete, cartaz) trocam pose/seed com `tl.set` em tempos fixos: nunca `Math.random()` sem semente, senão cada render sai diferente.
- Nada de marcas, logos ou personagens reconhecíveis em nenhum estilo, inclusive blocos de montar e anime.