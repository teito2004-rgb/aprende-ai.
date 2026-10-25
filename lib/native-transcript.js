import {setTimeout as delay} from 'node:timers/promises';
export function createNativeTranscriptClient({fetcher=(...args)=>fetch(...args),wait=(ms,signal)=>delay(ms,undefined,{signal}),now=()=>Date.now(),minIntervalMs=1500}={}){
 let queue=Promise.resolve(),nextStart=0;
 return (url,key,signal)=>{
  const work=async()=>{
   for(let attempt=0;attempt<2;attempt++){
    signal?.throwIfAborted();
    const pause=Math.max(0,nextStart-now());if(pause)await wait(pause,signal);
    nextStart=now()+minIntervalMs;
    const response=await fetcher(url,{headers:{'x-api-key':key},signal:AbortSignal.any([signal||new AbortController().signal,AbortSignal.timeout(12000)]),redirect:'error'});
    if(response.status!==429||attempt===1)return {status:response.status,raw:response.status===200?await response.json():null};
    const header=response.headers.get('retry-after');
    const seconds=header===null?2:Number(header);
    const milliseconds=Number.isFinite(seconds)?seconds*1000:Math.max(0,Date.parse(header)-now());
    await response.body?.cancel();
    nextStart=Math.max(nextStart,now()+Math.min(8000,Math.max(1500,milliseconds||2000)));
   }
  };
  const result=queue.then(work,work);queue=result.then(()=>undefined,()=>undefined);return result;
 };
}
export const nativeTranscript=createNativeTranscriptClient();
