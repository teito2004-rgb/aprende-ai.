---
name: "escolher-motor-ia"
description: "Escolher qual IA/motor usar em cada etapa de um vídeo (imagem, alteração, vídeo com/sem fala, lip sync, copiar movimento, voz). Usar ao planejar ou produzir vídeos com IA."
---

# Escolher o motor de IA certo

Base: lista "Principais IAs" do Mundo Boss (Rick Miura), lida em 10/11/2026. Modelos mudam rápido: se Clayton citar um modelo mais novo, ou se a escolha for cara, confira a página https://appboss.rickmiura.com/ias antes de decidir.

Antes de recomendar, pergunte (ou deduza) três coisas: **tem fala?**, **em que idioma?**, **é conteúdo rápido de internet ou trabalho profissional/cliente?**

## 1. Gerar imagem
- **Nano Banana Pro (2K)** — padrão, 90% dos casos: rápido, consistente, bom custo-benefício. (Higgsfield ou Freepik)
- **Midjourney** — quando o objetivo é criatividade/originalidade em imagem nova. Não serve para alterar imagem.
- **Nano Banana 2** — alternativa consistente.
- **Seedream 5.0** — estilo desenho/animação infantil, planos ousados, mantém rosto. Cuidado: impõe estilo próprio.

## 2. Alterar parte de uma imagem (manter o resto igual)
1. **Nano Banana Pro (2K)** — o que melhor preserva o resto da imagem.
2. **ChatGPT Image 2** — plano B quando o Nano Banana erra ou está congestionado.
3. **Photoshop** — só para ajuste cirúrgico em job caro.

## 3. Vídeo SEM fala
- **Kling 2.6** — melhor custo-benefício, fiel ao frame de entrada, movimento natural. Não faz fala.
- **Kling 3.0** — mais natural e nítido, custo maior.

## 4. Vídeo COM fala
- **Seedance 2.0 / 2.5** — disparado o melhor em fala, atuação e nitidez (caro; custo sobe com duração e resolução).
- **Kling 3.0** — ótima atuação, mas só em inglês.
- **Veo 3.1 Fast** (Google Flow) — fala português do Brasil, bom custo, porém menos nitidez/detalhe.

## 5. Lip sync a partir de imagem + áudio
- **Seedance 2.5** — aceita até 50 referências (áudio, vídeo, imagem), lip sync natural.
- **Kling Avatar 2.0** — bom, exige áudio pronto.
- Obs.: nunca fica tão natural quanto gerar a fala direto.

## 6. Lip sync em vídeo pronto
- **DreamFace** — troca a boca, mas sem expressão: resultado meio fake (evitar).
- **Kling Motion Control** — melhor caminho se houver vídeo de referência com alguém atuando.

## 7. Copiar movimento de um vídeo para outro
- **Kling Motion Control** — vídeo de 3 a 15 s + frame com pose parecida. Perde um pouco de expressão.
- **Seedance 2.5 + depth map do DaVinci** — exportar o movimento em depth map (preto e branco) para não copiar a aparência do personagem.

## 8. Fluxos para CONTEÚDO (rápido, internet)
1. **Seedance em resolução baixa** — qualidade surpreendente com orçamento menor.
2. **Veo 3.1 Fast + descrição de voz fixa** — repetir a MESMA descrição detalhada de voz em todos os prompts.
3. **Kling 3.0 + legenda** — natural e detalhado, gerado em inglês e legendado.

## 9. Fluxos PROFISSIONAIS (cliente, mais tempo e custo)
1. **Seedance 2.0 em 4K ou 2.5 em 1080p** — com direção de cena; se a demanda pedir, somar dubladores.
2. **Kling 3.0 em inglês + dublador profissional** — melhor resultado hoje: gera em inglês, dublador assiste e dubla, troca o áudio.
3. **Veo 3.1 em português + ElevenLabs** — padronizar a voz do personagem no ElevenLabs (voz sempre igual).
4. **Dublagem antes + Kling Motion Control** — gravar a atuação com áudio/vídeo e usar como referência de movimento.

## Atalho de decisão
- Imagem → Nano Banana Pro (criativo: Midjourney; desenho: Seedream).
- Vídeo sem fala → Kling 2.6 (qualidade: Kling 3.0).
- Vídeo com fala em PT-BR → Seedance; orçamento curto → Veo 3.1 Fast; voz consistente → + ElevenLabs.
- Vídeo com fala, máxima qualidade → Kling 3.0 em inglês + dublador, ou Seedance 4K.
- Copiar movimento → Kling Motion Control.

## Fora desta lista
A página não cobre motores de **texto/roteiro** nem de **música/trilha**. Para roteiro, usar o próprio Claude (e as skills nico-pesquisa-roteiro / equipe-produtora); para voz, ElevenLabs; para trilha, avaliar com Clayton (ex.: Artlist, ElevenLabs).

Sempre diga em uma linha por que escolheu aquele motor e qual é a alternativa se ele falhar ou estourar o orçamento.