const models=['minimax/minimax-m3.1-flash','google/gemini-2.5-flash-lite'];
export default async function handler(req,res){
 res.setHeader('Cache-Control','no-store');
 if(req.method!=='POST')return res.status(405).json({error:'Método não permitido'});
 const key=process.env.AI_GATEWAY_API_KEY;
 if(!key)return res.status(503).json({error:'O Sargento precisa da variável AI_GATEWAY_API_KEY configurada na Vercel.'});
 const {topic,minutes}=req.body||{};
 if(typeof topic!=='string'||!topic.trim()||topic.length>180||![15,30,60,120,180].includes(Number(minutes)))return res.status(400).json({error:'Informe um tema e uma duração válida.'});
 const instruction=`Você é o Sargento, coordenador educacional do Aprende Aí. Coordene mentalmente papéis de pesquisador, curador, professor, treinador e inspetor. Gere em português brasileiro um curso sobre o tema do usuário com ${minutes} minutos totais. Retorne SOMENTE JSON válido: {"title":string,"objective":string,"modules":[{"title":string,"minutes":number,"explanation":string,"activity":string}],"quiz":[{"question":string,"options":[string,string,string],"correct":number,"explanation":string}],"searchQueries":[string,string,string],"safetyNote":string}. Faça 4 módulos com soma EXATA ${minutes}; 3 questões com índice correto 0..2. Explicações concretas, corretas, aplicáveis. Não invente links nem afirme que pesquisou a web: searchQueries são consultas sugeridas para o usuário procurar vídeos, NÃO fontes verificadas. Para assuntos perigosos, recomende profissional habilitado, evite instruções operacionais arriscadas. Para saúde, não diagnostique. Não inclua markdown.`;
 try{
  let response,raw;
  for(const model of models){
   response=await fetch('https://ai-gateway.vercel.sh/v1/chat/completions',{method:'POST',headers:{'Authorization':`Bearer ${key}`,'Content-Type':'application/json'},body:JSON.stringify({model,temperature:0.4,max_tokens:2500,messages:[{role:'system',content:instruction},{role:'user',content:topic.trim()}]})});
   if(response.ok){raw=await response.json();break;}
  }
  if(!raw)return res.status(502).json({error:'A IA não respondeu. Confira o modelo habilitado e os créditos da API.'});
  const content=raw.choices?.[0]?.message?.content||'';
  const parsed=JSON.parse(content.replace(/^```(?:json)?\s*|\s*```$/g,''));
  if(!Array.isArray(parsed.modules)||!Array.isArray(parsed.quiz)||parsed.modules.reduce((n,m)=>n+Number(m.minutes||0),0)!==Number(minutes))throw Error('Estrutura inválida');
  return res.status(200).json({course:parsed,generated:true,sourcesVerified:false});
 }catch(e){return res.status(502).json({error:'Falha na geração ou validação do curso. Tente novamente.'});}
}
