# 🎬 Diretor de Produção IA

Espaço de trabalho para gerenciar projetos audiovisuais, clientes, animações, roteiros, prompts, referências, prazos e entregas.

> **Regra de ouro:** nenhum crédito de ferramenta de IA é gasto sem sua autorização explícita. Veja `CLAUDE.md` e `ferramentas/politica-creditos.md`.

## Por onde começar

1. Abra o **[painel](painel.md)** — visão geral de tudo que está em andamento.
2. Cadastre um cliente: copie `clientes/_modelo-cliente.md` para `clientes/nome-do-cliente.md`.
3. Crie um projeto: `./novo-projeto.sh nome-do-projeto "Cliente"` (copia a pasta modelo e adiciona ao painel).
4. Registre prazos em `prazos/calendario.md` e entregas em `entregas/registro.md`.

## Estrutura

| Pasta | O que guarda |
|---|---|
| `painel.md` | Projetos ativos, próximos prazos, pendências e aprovações aguardando |
| `clientes/` | Uma ficha por cliente: contato, marca, preferências, histórico |
| `projetos/` | Uma pasta por projeto (briefing, roteiro, prompts, referências, cronograma, entregas) |
| `roteiros/` | Modelo de roteiro e roteiros avulsos / banco de ideias |
| `animacoes/` | Modelo de decupagem (shot list) e controle de animações por cena |
| `prompts/` | Biblioteca de prompts testados por ferramenta e estilo |
| `referencias/` | Moodboards, links e análises de referências visuais e sonoras |
| `prazos/` | Calendário geral de prazos de todos os projetos |
| `entregas/` | Registro de entregas, versões e aprovações |
| `ferramentas/` | Ferramentas de IA disponíveis, política e registro de créditos |

## Fluxo de um projeto

```
Briefing → Roteiro → Referências/Estilo → Decupagem → Prompts (aprovação) →
Geração (SÓ com autorização) → Montagem/Som → Revisão → Entrega → Aprovação do cliente
```

Status usados em todo o espaço: `🟦 Briefing` · `🟨 Pré-produção` · `🟧 Produção` · `🟪 Pós` · `🔍 Revisão cliente` · `✅ Entregue` · `⏸️ Pausado`
