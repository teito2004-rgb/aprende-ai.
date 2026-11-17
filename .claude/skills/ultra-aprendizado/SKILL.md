---
name: ultra-aprendizado
description: "Ultraaprendizado do Claude — método que o próprio Claude usa quando precisa aprender algo novo para trabalhar para o Clayton: uma ferramenta ou modelo de IA (Seedance, Higgsfield, ElevenLabs, HyperFrames…), uma API, uma técnica de edição/som/roteiro, o estilo de um cliente ou um assunto de pesquisa. Usar sempre que o Claude encontrar algo que não domina, errar a mesma coisa duas vezes, ou o Clayton disser 'aprende isso', 'estuda essa ferramenta', 'vai atrás de como funciona'. Baseado nos 9 princípios do livro Ultra-aprendizado (Scott H. Young) na versão do Clayton."
---

# Ultraaprendizado do Claude

**Objetivo:** aprender qualquer coisa de forma rápida, profunda e eficiente, e deixar o aprendizado guardado para as próximas sessões.

> "Aprender melhor vale mais do que estudar mais."

Base: versão do Clayton (17/11/2026) do livro *Ultra-aprendizado* (Scott H. Young), adaptada para o Claude. Não reproduz trechos do livro.

## O que muda quando quem aprende é o Claude

- **Não tenho memória entre conversas.** O que não for escrito se perde. Reter = registrar em `Clayton cerebro/05-aprendizados/` (no repositório) ou atualizar a skill do assunto.
- **Meu conhecimento envelhece.** Ferramentas de IA mudam todo mês. Para preço, modelo, limite ou parâmetro, a fonte oficial atual vale mais do que a minha memória.
- **Praticar pode custar dinheiro.** Gerar imagem, vídeo, voz etc. para "testar" gasta crédito do Clayton e só acontece com o "sim, pode gerar" dele (regra do CLAUDE.md). Praticar de graça: documentação, chamadas só de leitura, listar modelos e esquemas, código local, amostras pequenas.

## Princípios fundamentais (versão do Clayton, aplicada ao Claude)

**1. Metalearning (aprender a aprender).** Antes de mexer, definir por que, o que e como aprender, e montar o mapa.
- Qual é o objetivo? (A tarefa concreta que o Clayton pediu.)
- Quais competências preciso dominar? (Conceitos, fatos, procedimentos.)
- Quais recursos vou usar? Primeiro os aprendizados já registrados em `05-aprendizados/` e as skills existentes; depois a documentação oficial, os esquemas das ferramentas e as fontes verificáveis (o Nico ajuda na pesquisa).

**2. Foco.** Um problema por vez. Não abrir cinco frentes nem desviar da tarefa para estudar o que ela não pede.

**3. Direção.** Aprender fazendo a tarefa real, do jeito mais seguro e barato: chamada de leitura, teste local, amostra pequena. Quer entender uma API? Chame a de leitura. Quer entender um formato? Produza um exemplo e valide.

**4. Exercício (drill).** Quando algo falhar, isolar o pedaço que trava (o menor caso que reproduz o erro) e resolver só ele. Pergunta: "O que está me impedindo de avançar?"

**5. Recuperação.** Antes de consultar, escrever o que acho que é a resposta e depois conferir na fonte. Onde minha memória errou é exatamente o que precisa ir para o registro. Lembrar e conferir é melhor que confiar.

**6. Feedback.** Buscar retorno rápido e real: rodar, testar, medir, comparar com uma referência, perguntar ao Clayton. Revisão crítica pelo Chico e números pela Fran. Separar o ego: errou, corrige e registra.

**7. Retenção.** Escrever o aprendizado no formato abaixo, no mesmo dia. "Revisão espaçada", para mim, é ler o registro do assunto no começo de toda tarefa parecida. O que vira procedimento repetível vira skill, prompt na Biblioteca da Central ou checklist.

**8. Intuição.** Entender o porquê, não só a receita. Técnica Feynman:
1. Escreva o conceito.
2. Explique como para uma criança (ao Clayton, em linguagem simples).
3. Identifique as lacunas.
4. Reestude.
5. Explique novamente.

**9. Experimentação.** Depois que o básico funciona, testar uma alternativa (outro parâmetro, outra abordagem, outra ferramenta) e registrar qual ganhou e por quê. Com custo, só com autorização.

## Mentalidade
Aprender fazendo · errar rápido e barato · feedback sempre · registrar sempre · experimentar sem medo, mas sem gastar crédito sem permissão.

## Fórmula
Planejar → Focar → Praticar → Testar → Receber feedback → Revisar → Entender profundamente → Experimentar → Dominar → **Registrar**

## Fluxo

1. **Checar o que já sei.** Ler `Clayton cerebro/05-aprendizados/INDICE.md` e a skill do assunto, se existir.
2. **Mapa curto** (princípio 1), em 3 a 6 linhas: objetivo, o que preciso saber, fontes.
3. **Ciclo:** hipótese (o que acho) → teste seguro → resultado → ajuste. Isolar o gargalo quando travar.
4. **Explicar ao Clayton** em linguagem simples o que aprendi e o que ainda é dúvida.
5. **Registrar** em `Clayton cerebro/05-aprendizados/<tema>.md` (modelo abaixo) e acrescentar uma linha no `INDICE.md`. Se a sessão não puder gravar no repositório, entregar o registro na conversa para o Clayton salvar.
6. **Promover:** se o aprendizado for usado de novo, propor transformá-lo em skill ou em item da Biblioteca.

## Modelo de registro

```
# <Tema>
Data: AAAA-MM-DD · Contexto: <tarefa/projeto> · Status: confirmado | parcial | hipótese

## Em uma frase
<o essencial, como para uma criança>

## O que funciona
- <procedimento / parâmetro / regra> — fonte: <link ou teste feito, data>

## O que não funciona / armadilhas
- <erro que cometi e por quê>

## Dúvidas abertas
- <o que não consegui confirmar>

## Próxima vez
- <o que fazer primeiro>
```

## Checklist de cada aprendizado
- [ ] Li o que já estava registrado antes de começar.
- [ ] Trabalhei sem dispersar (um problema por vez).
- [ ] Pratiquei na tarefa real, de forma segura e sem gastar crédito sem autorização.
- [ ] Testei a minha hipótese contra a fonte ou o resultado.
- [ ] Corrigi os erros e anotei a causa.
- [ ] Expliquei ao Clayton em linguagem simples.
- [ ] Registrei em `05-aprendizados/` (ou entreguei o registro para salvar).

## Regras
- Fonte verificável para fatos que mudam (preço, versão, limite, parâmetro), com data. O que for dedução fica marcado como hipótese.
- Nunca dizer que aprendi ou testei algo que não testei.
- Padrão de um cliente vale só para aquele cliente.
- Créditos de IA só com "sim, pode gerar" para aquela chamada específica.
