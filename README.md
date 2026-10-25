# Aprende Aí

Aprenda o que quiser, no tempo que tiver.

Metodologia **CHA — Conhecimento Humano Aplicado**.

## Uso

Informe um assunto, escolha 15, 30, 60, 120 ou 180 minutos e seu nível. O Sargento pesquisa materiais externos e prepara cinco etapas: Compreender, Observar, Praticar, Responder e Consolidar. A interface oferece fontes externas, atividades, perguntas com feedback e progresso com anotações salvo no próprio navegador. A última trilha é recuperada ao reabrir a página.

## Arquitetura

O projeto existente foi mantido: `index.html` e uma função Node.js em `api/course.js`. O Sargento coordena funções especializadas, sem seis serviços independentes:

- Explorador: pesquisa real via ferramenta Perplexity do Vercel AI Gateway, em buscas separadas para vídeos e páginas.
- Curador: usa títulos e trechos retornados pela busca para selecionar até cinco fontes relevantes, evitando duplicatas e páginas de vendas.
- Professor: gera explicações específicas e atividades adaptadas ao nível e ao tempo escolhido, usando as fontes selecionadas.
- Treinador: valida perguntas e alternativas; a interface corrige as respostas com explicação.
- Designer: organiza os cinco módulos, distribui o tempo e associa apenas IDs de fontes realmente retornados pela pesquisa.
- Inspetor: tenta verificar respostas HTTP dos links, remove 404/410, valida estrutura, duração e referências. O Sargento pode solicitar uma nova geração quando a validação final falha.

Os URLs apresentados são copiados dos resultados de busca pelo servidor; a IA não pode acrescentar URLs próprios na composição do curso.

## Publicação e configuração

A branch `main` está ligada à Vercel. Dependências: Node.js >=22 e AI SDK 7.0.153, fixado no lockfile. Configure `AI_GATEWAY_API_KEY` somente como variável de ambiente do servidor. Nunca coloque chaves no HTML ou no repositório.

A pesquisa e os modelos consomem os créditos existentes no AI Gateway. Nenhuma compra ou alteração de orçamento é feita pelo código.

## Limites desta versão

A seleção usa metadados e trechos indexados; não equivale a assistir integralmente aos vídeos ou certificar a qualidade pedagógica das fontes. A duração dos módulos é um orçamento estimado de estudo, incluindo exercícios. A duração total dos vídeos ainda não é extraída automaticamente e aparece como indisponível nos dados. Links podem exigir login ou bloquear verificações automáticas; nesses casos a interface informa que o acesso não foi confirmado. O conteúdo externo abre na plataforma de origem. Instagram depende da disponibilidade de páginas públicas nos resultados; não há integração autenticada com a plataforma.

Cache de uma hora, deduplicação de solicitações simultâneas, limite de três gerações simultâneas e limite de oito gerações por IP em dez minutos são controles em memória por instância, não limites globais distribuídos. Contas, sincronização entre dispositivos, fiscalização distribuída e correção por IA de respostas abertas permanecem para evolução futura. Não há promessa de ensinar execução profissional completa de tarefas complexas em poucos minutos.
