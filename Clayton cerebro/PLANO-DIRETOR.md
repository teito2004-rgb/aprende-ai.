# Plano Diretor — como a produtora se organiza

Feito para quem tem ideia demais. A cabeça cria; o sistema guarda, separa e lembra. Clayton cria, e o Claude organiza.

## 1. As cinco gavetas

Tudo o que existe na produtora mora em uma destas gavetas, e só em uma.

| Gaveta | O que entra | Exemplo |
|---|---|---|
| **Caixa de entrada** | Qualquer coisa que saiu da cabeça e ainda não foi pensada. Sem filtro, sem formatação. | "Episódio do Nico sobre por que bocejo é contagioso" |
| **Ideias** | O que passou pela triagem e vale guardar, com status. | A mesma ideia, marcada como *avaliar* e com área *Nico Explica* |
| **Projetos** | Ideia que virou compromisso: tem entrega, prazo e próximo passo. **Máximo 3 ativos.** | "Nico Explica #07 — bocejo", entrega sexta |
| **Biblioteca** | O que funcionou e se reusa: skills, agentes, comandos, prompts, imagens de referência. | Prompt de personagem Seedance, skill `som-por-codigo` |
| **Arquivo** | O que acabou ou foi descartado. Nada se apaga; só sai da frente. | Projeto entregue, ideia que perdeu o sentido |

### Status de uma ideia
`semente` → `avaliar` → `aprovada` → `em produção` → `feita` (ou `arquivada` em qualquer ponto)

- **semente:** acabou de chegar.
- **avaliar:** vale um olhar mais sério (público, custo, encaixe).
- **aprovada:** vai ser feita, mas ainda não começou.
- **em produção:** virou projeto ativo.

### Áreas
Toda ideia, projeto e item da biblioteca leva uma área: **Nico Explica**, **Clientes**, **Produtora** (a empresa em si: processos, marca, vendas) ou **Pessoal**.

## 2. Os rituais

| Quando | Quanto tempo | O que fazer |
|---|---|---|
| **Na hora** | 10 segundos | Ideia surgiu → joga na Caixa de entrada (site, `/ideia`, ou um áudio pro Claude). Não organiza nada agora. |
| **Fim de cada conversa útil** | 1 minuto | `/resumo`. Se nasceu um prompt, skill ou comando que funcionou, vai para a Biblioteca. |
| **Toda segunda** | 30 minutos, com o Claude | `/triagem`: esvaziar a Caixa de entrada. Cada item vira ideia, projeto, biblioteca ou arquivo. Rever os 3 projetos ativos. |
| **Primeira segunda do mês** | 1 hora | `/plano-diretor`: rever metas do mês, o que deu resultado (Fran), o que entra e o que sai. Atualizar este documento se a regra mudou. |

## 3. As regras

1. **Capturar não é decidir.** Na hora, só anota. Decide na triagem.
2. **Três projetos ativos, no máximo.** Ideia nova e boa espera na gaveta *aprovada* até abrir vaga. É isso que faz as coisas terminarem.
3. **Uma casa para cada coisa.** O site *Central* é a fonte da verdade para ideias, projetos e biblioteca. O repositório guarda o método, as cópias das skills e os projetos de produção (`diretor-producao-ia/`).
4. **Prompt que funcionou vira ficha.** Título claro ("Personagem com voz fixa — Seedance"), categoria, para que serve, o texto e, se houver, a imagem de referência do resultado.
5. **Nome padrão.** Projetos: `area-tema` em minúsculas (ex.: `nico-bocejo`). Resumos: `AAAA-MM-DD_HHhMM_tema_claude.md`.
6. **Cliente é cliente.** Nada de um cliente vai para outro.
7. **Créditos de IA só com "sim, pode gerar"** para aquela chamada específica.

## 4. Onde cada coisa está

| Coisa | Onde |
|---|---|
| Ideias, projetos, prompts com imagem, catálogo visual | Site **Central** (privado, login do Claude) |
| Este método, agentes, skills, comandos | `Clayton cerebro/` neste repositório |
| Pastas de produção (briefing, roteiro, decupagem, entregas) | `diretor-producao-ia/projetos/` |
| Base completa com dados pessoais | PC: `Documents\Codex\Clayton cerebro` |
| Resumos de conversa | PC: `Clayton cerebro\04-conversas\resumos` |

## 5. Comandos

| Comando | Faz |
|---|---|
| `/ideia <texto>` | Põe na Caixa de entrada do site |
| `/triagem` | Ritual semanal: esvazia a Caixa de entrada com você |
| `/plano-diretor` | Ritual mensal |
| `/nico <pedido>` | Chama o Nico |
| `/resumo` | Resume a conversa antes do `/clear` |
