# Guia visual do Nico Explica (padrão dos episódios que mais funcionaram)
Data: 2026-11-17 · Fonte: vidIQ (Shorts mais populares + análise cena a cena de Tesla, Bocejo e Atenção; 35 créditos) · Status: confirmado

## Desempenho orgânico (vidIQ, 17/11/2026)
**Regra: analisar só resultado orgânico.** Tesla (2.947 views) foi impulsionado → fora da referência.
Meditar 1.680 · Bocejo 1.099 · Atenção 1.023 · Cômodo 880 · Memória falsa 843 · Voz 770/66 likes. Fracos: Starlink, BYD, pipoca, pessoa importante (<25 views).

## Referência principal: "Trânsito / engarrafamento fantasma" (teste em outro canal, 24 h)
>1.000 views (canal fazia 10–130), continuou assistindo 40% (média 18–25%), 71,8% visto, 27 s de média, ~38 s.
- Gancho em <3 s com situação universal + termo curioso.
- **Gráficos 3D isométricos limpos**, texto grande, animação mostrando o fenômeno (carros freando, luz de freio, onda).
- Narração rápida, sem pausa morta.
- Melhorar: **cartela final de 1–2 s** (era 5 s estática) ou assinatura falada com a animação ainda rodando, emendando em loop; dar ênfase visual ao clímax da solução (zoom, marcação gráfica).

## Layout de cada cena
- Fundo alternando **amarelo #FFDC44** e **creme #FFF9E9** a cada cena.
- **Título** no alto à esquerda (y≈300), 2 linhas curtas, Inter 900, ~84 px, frase que muda a cada cena.
- **Ilustração vetorial grande no centro** (y≈500–1020): contorno carvão grosso (8–10 px), preenchimento creme/branco, detalhes ciano #27CDE0, cantos arredondados, às vezes sombra deslocada.
- **Nota pequena** sob a ilustração (fonte/estudo · "ilustração").
- **Legenda**: pílula carvão com texto claro, 2–4 palavras, sincronizada com a fala. **Posição aprovada pelo Clayton: topo da pílula em y≈1375 no quadro 1080×1920** (15–20 px acima do episódio da Lua, que ficava em ≈1395). Medido nos prints do YouTube Shorts e do Instagram Reels, acima do nome do perfil.
- **Elementos de app**: botão de like (círculo ciano com polegar + pílula "deixa um like"), enquete com opções, caixa de comentário.
- **Ritmo**: cena nova a cada ~3–4 s; animação funcional (setas, barras enchendo, objetos entrando), nada decorativo.
- **Fim**: logo "nico explica" + slogan "O cotidiano faz mais sentido." por **1–2 s no máximo** (arquivo no PC: `kit-v1\logo-sem-fundo.png`).
- Duração dos que performam: 38–47 s. Roteiro de ~100–115 palavras.
- Próximo nível visual: experimentar o estilo 3D isométrico do vídeo do trânsito (skill estilos-de-animacao: isométrico/3D de objetos).

## O que o v1 do #26 errou
Texto dominando, ilustração pequena, cena a cada 7,5 s, legenda clara com borda no rodapé, 60 s de duração, sem logo.

## Implementação
`diretor-producao-ia/projetos/nico-26/tools/gerar_v2.py` é o modelo: FRASES com tempos medidos → legendas; lista de cenas com título, ilustração SVG, nota e animação.
