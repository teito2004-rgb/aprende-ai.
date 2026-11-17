# Guia visual do Nico Explica (padrão dos episódios que mais funcionaram)
Data: 2026-11-17 · Fonte: vidIQ (Shorts mais populares + análise cena a cena de Tesla, Bocejo e Atenção; 35 créditos) · Status: confirmado

## Desempenho (vidIQ, 17/11/2026)
Tesla carro voador 2.947 views/152 likes · Meditar 1.680 · Bocejo 1.099 · Atenção 1.023 · Cômodo 880 · Memória falsa 843 · Voz 770/66 likes. Fracos: Starlink, BYD, pipoca, pessoa importante (<25 views).

## Layout de cada cena
- Fundo alternando **amarelo #FFDC44** e **creme #FFF9E9** a cada cena.
- **Título** no alto à esquerda (y≈300), 2 linhas curtas, Inter 900, ~84 px, frase que muda a cada cena.
- **Ilustração vetorial grande no centro** (y≈500–1020): contorno carvão grosso (8–10 px), preenchimento creme/branco, detalhes ciano #27CDE0, cantos arredondados, às vezes sombra deslocada.
- **Nota pequena** sob a ilustração (fonte/estudo · "ilustração").
- **Legenda**: pílula carvão com texto claro, 2–4 palavras, centro (y≈1150), sincronizada com a fala.
- **Elementos de app**: botão de like (círculo ciano com polegar + pílula "deixa um like"), enquete com opções, caixa de comentário.
- **Ritmo**: cena nova a cada ~3–4 s; animação funcional (setas, barras enchendo, objetos entrando), nada decorativo.
- **Fim**: logo "nico explica" centralizada com o slogan "O cotidiano faz mais sentido." (arquivo do logo está no PC: `kit-v1\logo-sem-fundo.png`).
- Duração dos que performam: 38–47 s. Roteiro de ~100–115 palavras.

## O que o v1 do #26 errou
Texto dominando, ilustração pequena, cena a cada 7,5 s, legenda clara com borda no rodapé, 60 s de duração, sem logo.

## Implementação
`diretor-producao-ia/projetos/nico-26/tools/gerar_v2.py` é o modelo: FRASES com tempos medidos → legendas; lista de cenas com título, ilustração SVG, nota e animação.
