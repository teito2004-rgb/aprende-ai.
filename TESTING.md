# Verificação — 25/10/2026

Destino: https://aprende-ai-mu.vercel.app/

## Execução real

Foram enviadas requisições POST à função publicada, usando a integração existente. Os quatro temas produziram cursos com cinco etapas, três perguntas, fontes retornadas por pesquisa e soma exata do tempo solicitado:

| Tema | Tempo | Resultado |
| --- | --- | --- |
| Aprender a rebocar uma parede | 60 min | Curso gerado; vídeos do YouTube com respostas HTTP 200 |
| Aprender edição de vídeo com IA | 120 min | Curso gerado; artigos e vídeos específicos, com respostas HTTP 200 |
| Aprender a cuidar de um cachorro | 30 min | Curso gerado; materiais de cuidados e vídeo relacionado |
| Aprender sobre Deus | 60 min | Curso gerado; fontes religiosas e vídeos; uma fonte retornou 403 e foi apresentada como acesso não confirmado |

Os testes encontraram limites temporários HTTP 429. Foram acrescentados modelo alternativo, busca alternativa e mensagem específica de limite temporário. Uma verificação 200 confirma resposta HTTP, não a validade integral do conteúdo nem a ausência de restrições posteriores.

## Interface no navegador

Confirmados na página publicada: geração pelo formulário, renderização das cinco etapas, links de fontes, correção de pergunta com feedback, atualização de progresso para 1/5, anotação recuperada após recarregar, preferência de tema e recuperação da última trilha. O botão Assistir aqui abriu o player real do YouTube e exibiu o título e o canal do vídeo.

A interface mantém layout responsivo para telas pequenas. Não foi concluída uma execução em aparelho celular físico: o teste automatizado de viewport móvel local ficou bloqueado pela indisponibilidade do navegador Chromium. Isso não foi apresentado como teste móvel aprovado.

## Verificação do contrato

Validados localmente: rejeição de método e entrada inválidos, distribuição exata para 15/30/60/120/180 minutos, remoção de IDs de fontes inexistentes, deduplicação de fontes e rejeição de URLs perigosos e endereços privados.

## Limitações

Curadoria baseada em títulos e trechos; não equivale a revisão integral dos materiais. Fontes podem ter anúncios, login ou paywall que a checagem HTTP não detecta. Duração de estudo estimada; a duração total dos vídeos não é extraída automaticamente. Limites e cache são por instância. Não há correção por IA de respostas abertas nem sincronização entre dispositivos.
