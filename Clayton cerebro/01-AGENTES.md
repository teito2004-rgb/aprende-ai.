# Equipe de agentes

## Organograma
```
Clayton — chefe (dá a ordem, aprova o que é crucial, palavra final)
   │
Jarvis — diretor (o Claude): planeja, distribui, aprende, contrata, cobra, entrega
   │
Nico · Mayara · Jéssica · João · Téo · Natasha · Fran · Chico · Pablo · Picasso · (novos contratados)
```
Como o Jarvis trabalha e quando contrata: skill [`jarvis`](02-skills/personalizadas/jarvis/SKILL.md). Ordem direta: `/jarvis <ordem>`.

No Claude Code cada agente existe como **subagente** em `.claude/agents/<nome>.md` e pode trabalhar de verdade, inclusive em paralelo. No chat, são modos de trabalho que o Claude assume.

São **modos de trabalho** que o Claude assume quando você chama pelo nome. Não são agentes rodando sozinhos. Definição completa em [`02-skills/personalizadas/equipe-produtora/SKILL.md`](02-skills/personalizadas/equipe-produtora/SKILL.md).

| Agente | Função | Onde está | Como chamar |
|---|---|---|---|
| **Nico** | Investigador: pesquisa com fontes verificáveis, referências virais, base de roteiro | skill `nico-pesquisa-roteiro` | `/nico <pedido>` ou "Nico, pesquisa…" |
| **Nico Explica** | A série (Shorts/Reels): pauta → entrega | skill `nico-explica` | `/nico episódio sobre…` |
| **Mayara** | Especialista de nicho e público | `equipe-produtora` | "Mayara, …" |
| **Jéssica** | Analista de roteiro (estrutura, gancho, promessa) | `equipe-produtora` | "Jéssica, analisa…" |
| **João** | Direção audiovisual | `equipe-produtora` | "João, …" |
| **Natasha** | Sound design e mixagem (desde 03/11/2026) | `equipe-produtora` + `som-por-codigo` | "Natasha, …" |
| **Fran** | Analista de dados e métricas | `equipe-produtora` | "Fran, …" |
| **Chico** | Revisor crítico | `equipe-produtora` | "Chico, revisa…" |
| **Pablo** | Roteirista / editor de texto | `equipe-produtora` | "Pablo, escreve…" |
| **Téo** | Produção e montagem do vídeo: prompts de geração, HyperFrames, animação, render (contratado pelo Jarvis em 17/11/2026) | `.claude/agents/teo.md` + seedance-boss, estilos-de-animacao, hyperframes | "Téo, monta…" |
| **Picasso** | UI/UX e tipografia (desde 30/10/2026) | `equipe-produtora` | "Picasso, …" |

## Fluxo de referência
Ordem do Clayton → **Jarvis** → **Nico + Mayara** → **Jéssica / João / Fran** → **Chico** → **Pablo** → revisão → **Picasso** (se houver visual) → **Téo** (produz o vídeo) → **Natasha** (som) → aprovação do Clayton → produção → entrega → resultados para Fran e Nico.

Mobilizar só quem o pedido precisa e nunca dizer que um perfil participou sem ter feito o trabalho.
