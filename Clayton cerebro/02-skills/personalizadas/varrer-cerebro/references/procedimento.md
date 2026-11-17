# Incorporação, estado e continuidade

## Onde cada achado vai

| Tipo de achado | Destino | Cuidado |
|---|---|---|
| Skill já existente, alterada | `02-skills/...` | Guardar a versão antiga em `09-varreduras/versoes/` com a data; registrar a atualização. |
| Nova skill definida e aprovada pelo usuário | Criar a skill (usar o skill-creator), espelhar em `02-skills/compartilhadas/`, guardar a origem em `references/origem.md` | Escopo específico; a skill não amplia permissões, agendamento nem ações externas. |
| Preferência ou aprendizado de cliente | Referência daquele cliente | Não virar regra geral. |
| Agente novo ou função alterada | `01-AGENTES.md` | Perfil reutilizável, não serviço em execução. |
| Programa/script | `06-programas-e-scripts/INDICE.md` | Registrar propósito, caminho, dependências e verificação existente; não executar só para catalogar. |
| Projeto/chat | `04-conversas/CATALOGO.md` | Distinguir leitura parcial de integral. |
| Contradição | Manter as duas fontes | Apontar a decisão mais recente só se for claramente substitutiva; senão deixar pendente. |

Atualizar `01-AGENTES.md`, `02-SKILLS.md` e os índices somente quando houver mudança pertinente. Depois, conferir links locais e o frontmatter das skills criadas.

## Chats (ChatGPT/Codex)

Neste ambiente os chats só chegam como arquivos enviados (exportações em JSON). Tratar assim:

- Registrar, por chat: ID, título, data de atualização, turnos lidos e cobertura (`parcial`, `completa` ou `indisponível`) em `09-varreduras/estado-chats.json`.
- Uma lista só com títulos e metadados é descoberta, não leitura. Os chats dela ficam como `parcial` ou `indisponível` até que o conteúdo seja enviado.
- Marcar limitações quando faltarem anexos ("file contents were not included"), houver truncamento ou só as falas do usuário.
- Em execuções seguintes, ler os chats novos ou alterados e retomar os parciais, sem repetir o que já foi revisado.

## Arquivos e Word

`scripts/inventariar.py` grava em `09-varreduras/estado-arquivos.json`. Depois da análise semântica, atualizar `reviewed_sha256` com o hash realmente revisado e guardar os achados. Se o conteúdo mudar, o script mantém a revisão como pendente.

Opções do script: `--root` (repetível; padrão: pasta atual), `--brain` (padrão: `./Clayton cerebro`, ou a variável `CEREBRO_DIR`). O script ignora dependências (`node_modules`, `.venv` etc.) e a própria base, para não haver recursão.

## Continuidade

Se a execução parar no meio (limite de tempo ou de contexto), gravar o estado e a fila, marcar a execução como parcial e dizer ao usuário o que falta. O chat de varredura não deve gerar novas descobertas a partir dos próprios relatórios.
