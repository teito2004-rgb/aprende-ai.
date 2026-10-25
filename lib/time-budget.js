export function isVideo(source){
 if(['YouTube','Instagram','Facebook'].includes(source.platform))return true;
 try{return /(^|\.)(youtube\.com|youtu\.be|instagram\.com|facebook\.com|fb\.watch)$/.test(new URL(source.url).hostname)}catch{return false}
}
export function videoSeconds(source){
 const clip=source.clip;
 if(['transcript','chapter'].includes(clip?.basis)&&Number.isFinite(clip.startSeconds)&&Number.isFinite(clip.endSeconds)&&clip.startSeconds>=0&&clip.endSeconds>clip.startSeconds)return clip.endSeconds-clip.startSeconds;
 const seconds=Number(source.durationSeconds);
 return Number.isFinite(seconds)&&seconds>0?seconds:null;
}
export function fitsVideoBudget(source,budgetSeconds){return !isVideo(source)||(videoSeconds(source)!==null&&videoSeconds(source)<=budgetSeconds)}
export function moduleVideoSeconds(sources){return sources.reduce((sum,s)=>sum+(isVideo(s)?videoSeconds(s)??Infinity:0),0)}
