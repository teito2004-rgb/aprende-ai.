export function isFreeLearningSource(source){
 try{
  const u=new URL(source.url);const host=u.hostname.toLowerCase().replace(/^www\./,'');
  if(u.protocol!=='https:')return false;
  if(/^(books\.google\.|play\.google\.)/.test(host))return false;
  if(/(^|\.)(amazon\.[a-z.]+|amzn\.to|audible\.[a-z.]+|everand\.com|scribd\.com|udemy\.com|hotmart\.com|kiwify\.com\.br|eduzz\.com|goodreads\.com|skoob\.com\.br|estantevirtual\.com\.br|kobo\.com)$/.test(host))return false;
  if(/\/(checkout|marketplace|cart|carrinho|comprar|buy|assinatura)(\/|\?|$)/i.test(u.pathname))return false;
  const text=[source.title,source.excerpt].filter(v=>typeof v==='string').join(' ').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  if(/(compre (este|o) (livro|curso)|assine para (ler|continuar)|conteudo exclusivo para assinantes|purchase (this|the) (book|course)|subscription required|buy this book)/.test(text))return false;
  return true;
 }catch{return false}
}
