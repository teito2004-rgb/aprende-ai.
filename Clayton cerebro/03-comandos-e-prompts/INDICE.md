# Comandos, regras e prompts

## Comandos de barra
| Comando | O que faz | Onde funciona | Arquivo |
|---|---|---|---|
| `/nico <pedido>` | Chama o Nico: episódio do Nico Explica → `nico-explica`; outra pesquisa → `nico-pesquisa-roteiro`; outros perfis → `equipe-produtora` | Claude Code com este repositório | [nico.md](nico.md) (cópia de `.claude/commands/nico.md`) |
| `/ideia <texto>` | Joga na caixa de entrada da Central | Claude Code com este repo | [ideia.md](ideia.md) |
| `/triagem` | Ritual de segunda | Claude Code com este repo | [triagem.md](triagem.md) |
| `/plano-diretor` | Ritual mensal | Claude Code com este repo | [plano-diretor.md](plano-diretor.md) |
| `/resumo` · `/resumo retomar` · `/resumo buscar` | Resumo da conversa no cérebro | Qualquer lugar com a skill `resumo` | skill `resumo` |

## Regras fixas (valem em toda conversa)
- **Créditos de IA:** nunca gerar imagem, vídeo, voz, música, lip sync, upscale, GPU etc. sem um "sim, pode gerar" para aquela chamada. Mostrar antes ferramenta, modelo, variações, custo e prompt. Registro em `diretor-producao-ia/ferramentas/registro-creditos.md`. Fonte: `CLAUDE.md` da raiz.
- **Agentes:** só mobilizar quem o pedido exige; não fingir participação.
- **Clientes:** identidade, chaves e material de um cliente nunca vão para outro.

## Biblioteca de prompts
- Prompts que funcionaram: [`diretor-producao-ia/prompts/biblioteca.md`](../../diretor-producao-ia/prompts/biblioteca.md) (ainda vazia: modelo pronto para preencher).
- Prompts de vídeo Seedance: modelos dentro de `02-skills/personalizadas/seedance-boss/SKILL.md`.
- Prompts por projeto: `diretor-producao-ia/projetos/<projeto>/prompts.md`.
