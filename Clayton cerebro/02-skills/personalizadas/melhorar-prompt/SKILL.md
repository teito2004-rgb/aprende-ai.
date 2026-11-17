---
name: "melhorar-prompt"
description: "Criar, revisar ou reescrever prompts para o Claude com boas práticas (contexto, exemplos, estrutura, papel, formato). Usar quando Clayton pedir para melhorar, montar ou avaliar um prompt."
---

# Melhorar prompt

Transforma um pedido vago num prompt claro, específico e reutilizável, com base no guia de prompting do Claude.

## Quando usar
- Clayton cola um prompt e pede para melhorar, revisar ou avaliar.
- Clayton descreve uma tarefa e pede "monta um prompt pra isso".
- Antes de mandar um pedido grande para outro agente/skill (Nico, equipe-produtora etc.), quando o pedido estiver vago.

## Processo

1. **Entender o objetivo.** Identifique: tarefa, para quem é o resultado, onde ele vai ser usado e o que conta como sucesso. Se faltar algo que muda o resultado (público, formato, tamanho), pergunte UMA vez, de forma curta. Se der para inferir, infira e diga o que assumiu.

2. **Diagnosticar o prompt original** contra este checklist:
   - Tarefa declarada logo no início?
   - Contexto suficiente (projeto, cliente, nicho, por que isso importa)?
   - Público definido?
   - Tom e estilo descritos (ou guia de estilo citado)?
   - Exemplo do resultado desejado (bom e, se útil, ruim)?
   - Estrutura de saída definida (seções, tópicos, tabela, nº de itens, tamanho)?
   - Tarefa complexa quebrada em etapas?
   - Pede raciocínio passo a passo quando o problema é complexo?
   - Papel/perspectiva útil atribuído (ex.: "como roteirista de Reels", "como CFO")?
   - Documentos citados pelo nome, com pedido de citação/trecho quando for análise?
   - Permissão explícita para dizer "não sei" quando há risco de inventar?

3. **Reescrever** aplicando só o que faltou — não inflar o prompt com itens irrelevantes. Ordem recomendada:
   1. Papel (se ajudar)
   2. Tarefa em uma frase
   3. Contexto e público
   4. Requisitos numerados (o que cobrir)
   5. Tom/estilo
   6. Formato de saída e tamanho
   7. Exemplo (se houver)
   8. Etapas finais (resumo, perguntas prováveis, riscos) quando fizer sentido
   9. "Se não tiver certeza de algo, diga que não sabe." quando houver fatos em jogo

4. **Entregar** neste formato:
   - **Prompt pronto** (em bloco de código, para copiar)
   - **O que mudou** — 3 a 5 bullets curtos, cada um com o porquê
   - **Variáveis para preencher** — campos entre [colchetes] que Clayton precisa completar, se houver

## Regras
- Manter o idioma em que o prompt vai ser usado (padrão: português).
- Preservar a intenção original; não mudar o objetivo da tarefa.
- Preferir requisitos concretos ("3 ganchos de até 8 palavras") a adjetivos ("ganchos bons").
- Para refinamento de uma resposta já gerada, montar feedback específico ("ajuste X para ficar mais Y") em vez de "melhora isso".
- Para tarefas longas demais, sugerir dividir em mensagens/etapas e entregar o prompt da primeira etapa.
- Lembrar que cada conversa nova não tem memória da anterior: o prompt deve trazer todo o contexto necessário.

## Exemplo rápido

Ruim: "Faz um roteiro sobre juros."

Bom:
```
Você é roteirista de Shorts de educação financeira.
Escreva um roteiro de 45 segundos explicando juros compostos para jovens de 18–25 anos que nunca investiram.
Requisitos:
1. Gancho nos primeiros 3 segundos (máx. 10 palavras)
2. Um exemplo com valores em reais
3. Uma analogia do dia a dia
4. Fechamento com chamada para seguir o perfil
Tom: leve, direto, sem jargão.
Formato: tabela com colunas Tempo | Fala | Visual.
Se algum número exigir dado atual, marque [CONFERIR] em vez de inventar.
```