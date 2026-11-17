---
description: Joga uma ideia na caixa de entrada da Central, sem organizar
argument-hint: "<a ideia, do jeito que vier>"
---

Ideia do Clayton: $ARGUMENTS

Grave na Central (artifact https://claude.ai/artifact/UMWoiUdGLBx8xvVFRqPzAt) com a ferramenta ArtifactData, ação "set", coleção "itens", um documento novo com id `ideia-<AAAAMMDD-HHMM>` e os campos: tipo "ideia", status "entrada", titulo (a ideia em até 12 palavras), resumo (o resto do texto, se houver), area (Nico Explica, Clientes, Produtora ou Pessoal; na dúvida, Produtora), origem "/ideia", imagens [], criadoEm e atualizadoEm (agora, ISO).

Não organize, não avalie, não sugira nada. Responda em uma linha: "Na caixa: <título>". Se a Central não estiver acessível, salve em `Clayton cerebro/caixa-de-entrada.md` e avise.
