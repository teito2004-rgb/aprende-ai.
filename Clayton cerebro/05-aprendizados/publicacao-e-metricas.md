# Publicar e medir os vídeos do Nico Explica
Data: 2026-11-17 · Contexto: publicação do #26 · Status: confirmado (exceto YouTube Nico)

## Em uma frase
Metricool publica Instagram + Facebook e mede retenção de graça; o YouTube do Nico ainda sai pelo vidIQ.

## Contas (Metricool, marca "claytonmartim", blogId 7688152, fuso America/Sao_Paulo)
- Instagram: @nicoexplica2026 · Facebook: Página 1476715702183017 · YouTube: **Clayton Martim** (não é o canal do Nico).
- vidIQ: YouTube Nico explica (UCwr8ipPxG_oalAw9Mv4LZQg) e Instagram conectados. Facebook do Nico **não** conecta no vidIQ (Página só via Meta Business).

## Melhor caminho
| Tarefa | Ferramenta | Custo |
|---|---|---|
| Publicar/agendar Instagram + Facebook | Metricool `createScheduledPost` (Reel; mídia = URL pública do MP4) | grátis |
| Publicar YouTube Nico | vidIQ `social_post_draft_create` + `publish` (pede verificação MFA do Clayton) | grátis |
| Retenção Instagram (% assistido, pulo em 3 s, view rate) | Metricool IGRE27/IGRE30/IGRE28 ou vidIQ `instagram_owner_insights` | grátis |
| Retenção YouTube Nico | vidIQ `channel_analytics` (audience_retention) | 5 créditos/consulta |
| Melhor horário | Metricool `getBestTimeToPostByNetwork` | grátis |
| Subir MP4 para ter URL pública | vidIQ `video_upload` localFile | grátis |

## Melhores horários (Metricool, semana de 17/11/2026, horário de Brasília)
- Instagram: **10h** (pico), **12h**, **18h**. Fim de semana bem mais fraco.
- Facebook: **10h**, **12h**, **17h**.
- Grade para 3 posts/dia: **10h, 12h30, 18h**.

## Armadilhas
- Verificação do YouTube no vidIQ pode travar na página: refazer em aba anônima, conta dona do canal.
- Links de conexão do Facebook (vidIQ) valem uma vez.
- Retenção é a métrica nº 1 (regra do Clayton); clique vem depois.

## Próxima vez
- Trocar o YouTube da marca no Metricool para o canal Nico explica → tudo num lugar só, sem crédito.
