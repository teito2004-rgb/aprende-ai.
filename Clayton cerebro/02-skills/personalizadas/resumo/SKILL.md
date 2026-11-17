---
name: "resumo"
description: "Sistema de economia de contexto compartilhado com o ChatGPT: resumir e salvar a conversa em Clayton cerebro/04-conversas/resumos antes do /clear, retomar do último resumo (Claude ou ChatGPT) e buscar em resumos antigos. Usar com /resumo, /resumo retomar ou /resumo buscar."
---

# /resumo — sistema de economia de contexto

Ideia: conversa longa custa caro porque todo o histórico é relido a cada mensagem. O ciclo é:
1. `/resumo` → salva só o essencial na pasta.
2. Clayton digita `/clear` (só ele pode; nenhuma skill limpa a conversa).
3. `/resumo retomar` → a conversa nova lê só o último resumo e continua.
4. `/resumo buscar <assunto>` → quando precisar de algo antigo, consulta os resumos sob demanda.

A pasta é compartilhada com o ChatGPT (sincronizada pelo Google Drive): o ChatGPT também deixa resumos nela, com o mesmo formato e sufixo `_chatgpt`. Tratar os dois como uma memória só.

## Onde salvar

- Pasta: `%USERPROFILE%\Documents\Codex\Clayton cerebro\04-conversas\resumos\` (criar a subpasta `resumos` se não existir).
- Se a pasta Clayton cerebro não estiver conectada nesta conversa, pedir acesso a ela pelo acesso a pastas do computador. Se não for possível, gerar o arquivo e enviar na conversa, avisando que não foi salvo no PC.

---

## Modo 1 — `/resumo` (salvar)

Objetivo: Clayton vai limpar o contexto. O resumo precisa permitir que uma conversa NOVA, lendo só este arquivo, continue o trabalho sem perder nada importante.

- Nome: `AAAA-MM-DD_HHhMM_assunto-curto_claude.md` (data e hora de São Paulo; pegar com a ferramenta de hora atual; assunto em minúsculas, com hífens, sem acento). Ex.: `2026-11-09_11h50_episodio-nico-inflacao_claude.md`.
- Nunca sobrescrever um resumo existente; cada resumo é um arquivo novo.
- Se vier texto junto do comando (ex.: `/resumo só o roteiro e a voz`), priorizar esse foco e deixar o resto em uma linha.

Formato do arquivo:

```markdown
# Resumo — <assunto>
Data: <data e hora> | Origem: Claude | Projeto/cliente: <nome ou "geral"> | Resumo anterior: <nome do arquivo ou "nenhum">

## Objetivo
O que estávamos tentando fazer, em 1–2 frases.

## Decisões tomadas
- Decisão + motivo curto (o que foi aprovado, rejeitado, escolhido).

## Estado atual
Onde o trabalho parou exatamente.

## Pendências / próximos passos
- [ ] Próxima ação concreta (quem faz, se for de alguém da equipe).

## Arquivos e links
- Caminho ou link de cada arquivo criado/usado, com uma linha dizendo o que é.

## Instruções e preferências dadas nesta conversa
- Regras de estilo, voz, formato, tom que Clayton pediu e que devem valer na continuação.

## Para retomar
/resumo retomar
```

Regras:
- Escrever em português, direto, sem enrolação. Seções vazias: escrever "nada" em vez de inventar. Alvo: até ~1 página.
- Se esta conversa começou de um resumo anterior, o novo resumo já incorpora o que ainda vale do anterior (pendências abertas, preferências) — assim basta ler sempre o último. Itens resolvidos saem.
- Registrar decisões e conteúdos finais (ex.: versão aprovada do roteiro, nome da voz, IDs de geração), não o vaivém da conversa.
- Textos curtos aprovados (título, gancho, legenda) podem ir inteiros; textos longos ficam no arquivo deles e o resumo aponta o caminho.
- Nunca incluir senhas, chaves de API ou tokens.
- Antes de resumir, se houver na pasta um resumo do mesmo projeto mais recente que o desta conversa (inclusive do ChatGPT), incorporar o que ainda vale dele também.
- Depois de salvar, atualizar o `INDICE.md` da pasta resumos (criar se não existir): acrescentar a linha do novo arquivo e também de qualquer arquivo da pasta que ainda não esteja no índice (ex.: resumos do ChatGPT). Formato: `- AAAA-MM-DD HHhMM — <assunto> — <projeto> — <origem> — <arquivo>`.
- Ao terminar, responder em 2 linhas: "Salvo em resumos/<arquivo>. Agora é só digitar /clear e depois /resumo retomar."

## Modo 2 — `/resumo retomar`

- Listar a pasta resumos (não confiar só no `INDICE.md`, que pode não ter os resumos do ChatGPT) e abrir só o mais recente pela data no nome, seja de Claude ou do ChatGPT (ou o que Clayton indicar pelo assunto). Dizer de qual origem ele veio.
- Se o projeto tiver resumos recentes das duas origens, abrir o último de cada uma.
- Não abrir resumos antigos nem outros arquivos do cérebro sem necessidade — o objetivo é gastar pouco.
- Responder curto: em 3–4 linhas, onde paramos e qual é o próximo passo, e seguir com o trabalho.
- Também vale quando Clayton disser "continua de onde paramos" no início de uma conversa.

## Modo 3 — `/resumo buscar <assunto>`

- Procurar o assunto no `INDICE.md` e nos nomes dos arquivos e, se preciso, buscar o termo dentro dos arquivos de resumos de ambas as origens (busca por texto, sem abrir tudo).
- Abrir só os resumos relevantes e trazer a informação pedida, dizendo de qual arquivo veio.

## Lembrete de economia

Quando esta skill já estiver em uso numa conversa e ela ficar longa (muitas trocas, arquivos grandes lidos, uma etapa concluída), sugerir em uma linha: "A conversa está grande — quer fazer /resumo e limpar?". No máximo uma vez por etapa; não insistir.