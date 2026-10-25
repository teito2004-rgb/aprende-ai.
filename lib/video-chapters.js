function seconds(value){
 if(typeof value!=='string'||!/^\d{1,3}:\d{2}(?::\d{2})?$/.test(value))return null;
 const parts=value.split(':').map(Number);if(parts.slice(1).some(n=>n>59))return null;
 return parts.reduce((n,v)=>n*60+v,0);
}
export function extractChapters(player,durationSeconds){
 const points=[];
 // Chapters embedded in the public player response.
 const stack=[player];let visited=0;
 while(stack.length&&visited++<30000){const node=stack.pop();if(!node||typeof node!=='object')continue;
  const c=node.chapterRenderer;
  if(c){const start=Number(c.timeRangeStartMillis)/1000;const title=c.title?.simpleText||c.title?.runs?.map(r=>r.text).join('');if(Number.isFinite(start)&&start>=0&&title)points.push({start,title});}
  const m=node.macroMarkersListItemRenderer;
  if(m){const raw=m.onTap?.watchEndpoint?.startTimeSeconds ?? m.onTap?.innertubeCommand?.watchEndpoint?.startTimeSeconds ?? seconds(m.timeDescription?.simpleText);const start=raw==null?NaN:Number(raw);const title=m.title?.simpleText||m.title?.runs?.map(r=>r.text).join('');if(Number.isFinite(start)&&start>=0&&title)points.push({start,title});}
  for(const child of Object.values(node))if(child&&typeof child==='object')stack.push(child);
 }
 // Explicit timestamp lines supplied in the video's public description.
 for(const line of (player?.videoDetails?.shortDescription||'').split('\n')){
  const match=line.trim().match(/^(\d{1,3}:\d{2}(?::\d{2})?)\s*(?:[-–—|]\s*)?(.{2,200})$/);
  if(match){const start=seconds(match[1]);if(start!==null)points.push({start,title:match[2]});}
 }
 const unique=[...new Map(points.map(p=>[p.start,p])).values()].filter(p=>p.start>=0&&(!durationSeconds||p.start<durationSeconds)).sort((a,b)=>a.start-b.start).slice(0,100);
 if(unique.length<2)return [];
 return unique.flatMap((point,i)=>{const end=unique[i+1]?.start??durationSeconds;return Number.isFinite(end)&&end>point.start?[{id:'c'+i,start:point.start,end,title:String(point.title).slice(0,200)}]:[]});
}
export function chapterClip(source,selection,maxSeconds){
 if(!selection||typeof selection!=='object'||!Array.isArray(source.chapters))return null;
 const from=source.chapters.findIndex(c=>c.id===selection.from),to=source.chapters.findIndex(c=>c.id===selection.to);
 if(from<0||to<from)return null;
 const first=source.chapters[from],last=source.chapters[to];
 const start=Math.floor(first.start),end=Math.ceil(last.end);
 if(!Number.isFinite(start)||!Number.isFinite(end)||start<0||end<=start||end-start>maxSeconds)return null;
 return {startSeconds:start,endSeconds:end,basis:'chapter',label:'Trecho selecionado pelo capítulo',chapterTitle:first.title};
}
