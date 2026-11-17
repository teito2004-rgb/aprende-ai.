# Catálogo de skills

Cópias em `02-skills/personalizadas/<nome>/`. No Claude.ai elas aparecem como `anthropic-skills:<nome>`. Hash = primeiros 12 caracteres do SHA-256 do SKILL.md original no dia da cópia.

## Suas skills (personalizadas)

| Skill | Para que serve | Chamar com | Hash (17/11/2026) |
|---|---|---|---|
| [jarvis](02-skills/personalizadas/jarvis/SKILL.md) | O Claude como diretor: planeja, distribui para a equipe, contrata agentes/skills, presta contas. Para o chat: suba `02-skills/jarvis.zip`. | "Jarvis, …" · `/jarvis` | nova |
| [equipe-produtora](02-skills/personalizadas/equipe-produtora/SKILL.md) | Perfis da equipe (Mayara, Jéssica, João, Natasha, Fran, Chico, Pablo, Picasso) | nome do agente | 5122edee7671* |
| [nico-pesquisa-roteiro](02-skills/personalizadas/nico-pesquisa-roteiro/SKILL.md) | Nico investigador: pesquisa rastreável e roteiro para Reels/Shorts de qualquer nicho | `/nico`, "Nico, …" | 8af064ef3d7d* |
| [nico-explica](02-skills/personalizadas/nico-explica/SKILL.md) | Série Nico Explica de ponta a ponta (pauta → vídeo HyperFrames → entrega) | `/nico episódio…` | 4c8ad0127059* |
| [seedance-boss](02-skills/personalizadas/seedance-boss/SKILL.md) | Sistema de prompts Seedance 2.5 (cortes de cinema, @tags Higgsfield, atuação por fala) | "prompt Seedance…" | 103167cc9b21 |
| [escolher-motor-ia](02-skills/personalizadas/escolher-motor-ia/SKILL.md) | Qual IA usar em cada etapa (imagem, vídeo com/sem fala, lip sync, voz) | "qual IA uso pra…" | 8db92eca8526 |
| [estilos-de-animacao](02-skills/personalizadas/estilos-de-animacao/SKILL.md) | 17 estilos de animação no HyperFrames, 9:16 | "anima em estilo…" | 9810421c0046 |
| [som-por-codigo](02-skills/personalizadas/som-por-codigo/SKILL.md) | Trilha, efeitos e mixagem por Python com ducking e LUFS | "faz o som…" | 8016e3f2db50* |
| [melhorar-prompt](02-skills/personalizadas/melhorar-prompt/SKILL.md) | Criar/revisar prompts para o Claude | "melhora esse prompt" | 19c368a11552 |
| [resumo](02-skills/personalizadas/resumo/SKILL.md) | Resumo de conversa antes do /clear, retomar e buscar (compartilhado com ChatGPT) | `/resumo`, `/resumo retomar`, `/resumo buscar` | 1852d04f97f7* |
| [ultra-aprendizado](02-skills/personalizadas/ultra-aprendizado/SKILL.md) | **Usada pelo Claude** quando precisa aprender algo novo (ferramenta, técnica, cliente, assunto). Registra em `05-aprendizados/`. Para valer no chat, suba `02-skills/ultra-aprendizado.zip` em Configurações → Skills. | automática / "aprende isso" | nova |
| [varrer-cerebro](02-skills/personalizadas/varrer-cerebro/SKILL.md) | Varredura que atualiza este cérebro | "atualiza o cérebro" | b5cbb84e8076* |

\* Cópia com dados pessoais trocados por marcadores; o hash é do original completo.

## Skills padrão (vêm com o Claude, não estão copiadas)
docx, pdf, pptx, xlsx, docs, google-workspace, skill-creator, deep-research, morning, import-memory, artifact-emulator, built-in-browser, chrome-browser, computer-use. No Claude Code também há os plugins HyperFrames, Remotion, watch-video e surehand-ae.
