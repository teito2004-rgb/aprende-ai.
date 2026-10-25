const models = [
  'minimax/minimax-m3.1-flash',
  'google/gemini-2.5-flash-lite'
];

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');

  if (req.method !== 'POST') {
    return res.status(405).json({
      error: 'Método não permitido'
    });
  }

  const key = process.env.AI_GATEWAY_API_KEY;

  if (!key) {
    return res.status(503).json({
      error: 'O Sargento precisa da variável AI_GATEWAY_API_KEY configurada na Vercel.'
    });
  }

  const { topic, minutes } = req.body || {};

  if (
    typeof topic !== 'string' ||
    !topic.trim() ||
    topic.length > 180 ||
    ![15, 30, 60, 120, 180].includes(Number(minutes))
  ) {
    return res.status(400).json({
      error: 'Informe um tema e uma duração válida.'
    });
  }

  const instruction = `Você é o Sargento, coordenador educacional do Aprende Aí. Coordene mentalmente papéis de pesquisador, curador, professor, treinador e inspetor. Gere em português brasileiro um curso sobre o tema do usuário com ${minutes} minutos totais. Retorne SOMENTE JSON válido: {"title":string,"objective":string,"modules":[{"title":string,"minutes":number,"explanation":string,"activity":string}],"quiz":[{"question":string,"options":[string,string,string],"correct":number,"explanation":string}],"searchQueries":[string,string,string],"safetyNote":string}. Faça 4 módulos com soma EXATA ${minutes}; 3 questões com índice correto 0..2. Explicações concretas, corretas, aplicáveis. Não invente links nem afirme que pesquisou a web: searchQueries são consultas sugeridas para o usuário procurar vídeos, NÃO fontes verificadas. Para assuntos perigosos, recomende profissional habilitado, evite instruções operacionais arriscadas. Para saúde, não diagnostique. Não inclua markdown.`;

  try {
    let raw;

    for (const model of models) {
      const response = await fetch(
        'https://ai-gateway.vercel.sh/v1/chat/completions',
        {
          method: '
