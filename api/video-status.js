import { videoAvailability } from '../lib/video-availability.js';
export default async function handler(req,res){
 res.setHeader('Cache-Control','no-store');
 if(req.method!=='POST')return res.status(405).json({error:'Método não permitido'});
 const origin=req.headers?.origin;
 if(origin&&origin!=='https://'+req.headers.host&&origin!=='http://'+req.headers.host)return res.status(403).json({error:'Origem inválida'});
 const ids=req.body?.ids;
 if(!Array.isArray(ids)||ids.length<1||ids.length>10||ids.some(id=>typeof id!=='string'||!/^[A-Za-z0-9_-]{11}$/.test(id)))return res.status(400).json({error:'Vídeos inválidos'});
 const results=await Promise.all([...new Set(ids)].map(async id=>({id,...await videoAvailability(id)})));
 return res.status(200).json({videos:results});
}
