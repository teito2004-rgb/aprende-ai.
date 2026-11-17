---
name: "nico-explica"
description: "Produzir episódios da série Nico Explica (Shorts/Reels verticais) de ponta a ponta — pauta, pesquisa, roteiro, voz do Nico, vídeo no HyperFrames, som, conferência e entrega. Usar quando Clayton pedir um episódio, pauta, roteiro ou vídeo do Nico Explica."
---

# Nico Explica — produção da série

Série de Clayton no canal [link do canal] (Shorts, 1080×1920). Esta skill coordena a produção; a pesquisa segue `nico-pesquisa-roteiro` e as funções da equipe seguem `equipe-produtora`. Clayton dirige e aprova.

## Onde está tudo (computador do Clayton, Windows)

Acessar pelas ferramentas do computador conectado (pedir acesso à pasta se não estiver conectada; nunca supor o conteúdo):

- Base de projetos: `%USERPROFILE%\OneDrive\Documentos\ChatGPT\Clayton\` — `outputs\nico-<tema>\` (entregas) e `work\nico-<tema>\` (trabalho).
- Identidade e kit: `outputs\nico-identidade\` (IDENTIDADE.md, FLUXO-DE-ENTREGA.md, PRONUNCIAS-APROVADAS.md, `kit-v1\` com logos PNG, fontes Inter e GUIA-DE-USO.md).
- Pautas e aprendizados: `outputs\nico-pautas\` (PAUTAS-PUBLICO, BANCO-EXPERIENCIAS, ANALYTICS) e `outputs\nico-serie\RASCUNHOS.md`.
- Episódio de referência mais completo: `outputs\nico-byd\` (ROTEIRO-v1.md, projeto\SPEC.md, projeto\cenas.json, PUBLICACAO.txt).
- Pasta final de entrega: `%USERPROFILE%\OneDrive\Clayton\N\Nico Explica\` — uma subpasta numerada por vídeo (ex.: `14-nome-do-tema`).
- Base de conhecimento geral: `%USERPROFILE%\Documents\Codex\Clayton cerebro\`.

Antes de um episódio novo, ler IDENTIDADE.md, FLUXO-DE-ENTREGA.md, PRONUNCIAS-APROVADAS.md, a última entrega da série e o BANCO-EXPERIENCIAS se for episódio de experiência. Decisões mais recentes prevalecem sobre as antigas.

## Identidade (aprovada)

- Essência: **O cotidiano faz mais sentido.** Perguntas da vida comum viram explicações claras, visuais e com fonte.
- Territórios: você por dentro (percepção, atenção, memória, emoção); entre a gente (vínculos, comportamento); o estranho no comum; tecnologia concreta e curiosa (carro voador, BYD, Starlink, tornado).
- Tom: curioso, próximo, cuidadoso. Fala com "você", exemplo antes do termo técnico, uma ideia central por vídeo. Distinguir hipótese, associação e causa. Evitar "a ciência prova", "ninguém te conta", "hackear o cérebro", "cura", números sem fonte, tom professoral.
- Cores: amarelo #FFDC44, creme #FFF9E9, carvão #171B18, ciano #27CDE0. Texto em carvão sobre fundos claros; nunca branco sobre amarelo/ciano. Cenas alternam amarelo e creme.
- Tipografia nos vídeos: Inter local (arquivo em `kit-v1\fontes`, com @font-face). Títulos ~72–82px peso 800, legendas ~43px peso 550, notas/créditos ~29px. Caixa de sentença.
- Marca: logo raster "nico / explica" com ponto ciano no i (usar `logo-sem-fundo.png`; não redesenhar, não distorcer, não acrescentar símbolos). Encerramento com logo e assinatura **centralizadas**.
- Área útil: conteúdo em x≈120–900, y≈225–1300; legendas fora de rostos e dos controles da plataforma.

## Formatos de episódio

**Padrão (explicação):** abre pela pergunta no primeiro quadro (cena amarela com o texto da pergunta) → progressão em cenas curtas ligadas à fala → resposta entregue → fecho falado "Eu sou o Nico, e esse foi mais um Nico Explica." + logo centralizada. Duração típica 40–60 s, definida pela locução real.

**Série de experiências (participativa):** convida o espectador a fazer uma experiência na abertura; convite de like contextual no meio, depois que a pessoa tentou/percebeu; no fim, uma pergunta específica para comentário. Nesse formato o CTA substitui a assinatura falada e a cartela final. Não trocar a resposta por pedido genérico de inscrição. Respeitar que nem todos sentem o efeito; nada de flashes ou luz forte.

## Fluxo de um episódio

1. **Pauta** — partir do pedido ou de `nico-pautas`. Preferir perguntas concretas que o público reconhece em si (voz, meditação e carro foram os melhores totais públicos até 6/11; isso é hipótese, não regra). Se Clayton trouxer um vídeo de referência, analisar alegações antes de usar; o título da referência não é evidência.
2. **Pesquisa (Nico)** — seguir `nico-pesquisa-roteiro`: fontes primárias/institucionais com link e data, alegações liberadas e alegações barradas. Mostrar o que fica de fora e por quê.
3. **Roteiro (Pablo, revisado por Jéssica/Chico)** — fala completa + tabela de cenas (fala → imagem/ação → texto na tela → fonte). Apresentar para aprovação. **Não gerar voz nem vídeo antes de Clayton aprovar** ("pode produzir" ou equivalente).
4. **Voz** — "Nico — Voz original v1" no ElevenLabs, modelo Eleven v4, estabilidade 0,65, similaridade 0,75. Escrever o texto para voz aplicando PRONUNCIAS-APROVADAS (ex.: BYD → "Bi aí dí" na voz; na tela continua BYD). Gerar pelo navegador conectado na conta do Clayton; é geração paga: dizer quantos caracteres vão e confirmar antes, a menos que a aprovação do roteiro já tenha autorizado a produção. Usar a primeira tomada salvo problema; registrar créditos antes/depois. Guardar a tomada em `work\nico-<tema>\`.
5. **Tempos reais** — transcrever a locução (palavras com tempo) e cortar as cenas pela fala real. Contagem de palavras não define tempo.
6. **Vídeo (HyperFrames)** — carregar a skill `hyperframes` antes. Projeto 1080×1920, 30 fps, uma cena por sub-composição, nomes curtos em português (pergunta, baterias, motor…), `cenas.json` com [id, início, fim, texto, tipo, cor de fundo, nota]. Legendas embutidas a partir da transcrição + `legendas.srt`. Ilustrações e diagramas originais; fotos reais só com licença rastreável (Wikimedia/CC) e crédito curto na tela + completo na descrição. Movimentos finitos e determinísticos; título parado enquanto é lido; não repetir a mesma entrada em todas as cenas; nada de partículas decorativas ou objetos pequenos em fundo vazio. Escrever SPEC.md (GOAL, OUTPUT, LOOK, OBJECTS, MOTION, SHOTS, SOUND, BANNED, QA) antes de construir.
7. **Som (Natasha)** — seguir o perfil Natasha em `equipe-produtora`: fala em primeiro lugar, música discreta com ducking pela voz, efeitos só onde há ação na tela (encaixe, papel, ar…). Música/efeitos sintetizados localmente ou de catálogo licenciado, com origem registrada em `cue-sheet.json`. Ganho de voz perto de 0,85–0,94. Alvo interno do master: ≈ −16 LUFS ±1, teto −1,5 dBTP (escolha da produtora, não regra do YouTube).
8. **Conferência** — `hyperframes check` sem erros; folhas de contato em tamanho de celular de todas as cenas e transições; quadros decodificados do MP4 final nos pontos-chave; medir LUFS/true peak/LRA do AAC final; duração igual à composição. Escrever REVIEW.md. **Nunca afirmar que ouviu** o áudio: dizer que foi medido/transcrito e que a escuta final é do Clayton.
9. **Entrega** — em `outputs\nico-<tema>\`: MP4 final (`Nico-Explica-<Tema>.mp4`), `PUBLICACAO.txt` (título com emoji + "| Nico Explica", descrição fiel com ressalvas, FONTES, CRÉDITOS DAS IMAGENS, hashtags #NicoExplica … #Shorts), `legendas.srt`, `LOCUCAO.txt`, `ROTEIRO-PARA-VOZ.txt`, `cue-sheet.json`, `medicao-final.json`, `ENTREGA.md`, `projeto\`. Pasta de postagem `outputs\PRONTO-PARA-POSTAR-<Tema>\` só com MP4 + `Titulo-e-Descricao.txt`. Copiar MP4 e textos para `OneDrive\Clayton\N\Nico Explica\<NN-tema>\` e conferir (tamanho/hash).
10. **YouTube (rascunho)** — Clayton autorizou em 6/11/2026 subir cada vídeo final como **rascunho** no YouTube Studio do Nico Explica: preencher título, descrição com fontes, idioma português (Brasil), categoria Ciência e tecnologia, não é para crianças, sem promoção paga, conteúdo alterado/sintético declarado, comentários ativados; avançar até Visibilidade e **fechar sem publicar nem agendar**; conferir na lista que ficou "Rascunho". Neste ambiente, confirmar no chat antes do primeiro envio de cada sessão. Clayton publica um por dia.

## Limites

- Sem publicação, agendamento, mensagens a terceiros ou geração paga além da voz aprovada.
- Não inventar métricas, retenção ou motivos de desempenho. Resultados vão para Fran/Nico como hipóteses.
- Não aplicar a identidade do Nico a outros clientes ([Cliente A], [Cliente D] etc.) nem a deles ao Nico.
- Preservar versões anteriores ao refazer (v1, v2…); nunca sobrescrever entregas publicadas.