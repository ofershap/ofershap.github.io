(() => {
 const box=document.querySelector('.engagement');if(!box)return;
 const API='https://blog-engagement.ofers.workers.dev/stats', key=box.dataset.key;
 const messages={en:{copied:'Link copied.',failed:'Could not connect. Try again later.',liked:'Liked.',unliked:'Like removed.',need:'Likes need local browser storage.',copy:'Copy this link:'},he:{copied:'הקישור הועתק.',failed:'החיבור לא זמין כרגע. נסו שוב בהמשך.',liked:'הלייק נשמר.',unliked:'הלייק הוסר.',need:'לייקים דורשים שמירה מקומית בדפדפן.',copy:'העתיקו את הקישור:'}};
 messages.ar={copied:'تم نسخ الرابط.',failed:'الاتصال غير متاح حالياً. حاول لاحقاً.',liked:'تم تسجيل الإعجاب.',unliked:'تمت إزالة الإعجاب.',need:'يتطلب الإعجاب تخزيناً محلياً في المتصفح.',copy:'انسخ هذا الرابط:'};
 messages.es={copied:'Enlace copiado.',failed:'No se pudo conectar. Inténtalo más tarde.',liked:'Me gusta guardado.',unliked:'Me gusta eliminado.',need:'Los me gusta necesitan almacenamiento local.',copy:'Copia este enlace:'};
 messages['zh-Hans']={copied:'链接已复制。',failed:'暂时无法连接，请稍后重试。',liked:'已点赞。',unliked:'已取消点赞。',need:'点赞需要浏览器本地存储。',copy:'请复制此链接：'};
 const text=messages[box.dataset.lang]||messages.en, status=box.querySelector('.engagement-status');
 const canonical=document.querySelector('link[rel="canonical"]')?.href||location.href.split('?')[0];
 const title=document.querySelector('h1')?.textContent||document.title;
 box.querySelectorAll('[data-network]').forEach(a=>{a.href=a.dataset.network==='linkedin'?'https://www.linkedin.com/sharing/share-offsite/?url='+encodeURIComponent(canonical):'https://twitter.com/intent/tweet?url='+encodeURIComponent(canonical)+'&text='+encodeURIComponent(title);});
 const copy=async()=>{try{await navigator.clipboard.writeText(canonical);status.textContent=text.copied;}catch{status.textContent=text.copy+' '+canonical;}};
 box.querySelector('.engagement-copy').addEventListener('click',copy);
 box.querySelector('.engagement-share').addEventListener('click',async()=>{if(navigator.share){try{await navigator.share({title,url:canonical});}catch(e){if(e.name!=='AbortError')await copy();}}else await copy();});
 let client;
 try {client=localStorage.getItem('blog-client-v1');if(!/^[a-f0-9]{32}$/.test(client||'')){client=Array.from(crypto.getRandomValues(new Uint8Array(16))).map(v=>v.toString(16).padStart(2,'0')).join('');localStorage.setItem('blog-client-v1',client);}}catch{status.textContent=text.need;return;}
 const button=box.querySelector('.engagement-like');let liked=false;
 const views=document.createElement('span');views.className='engagement-views';views.hidden=true;box.querySelector('.engagement-actions').append(views);
 const viewLabels={en:'views',he:'צפיות',ar:'مشاهدات',es:'visitas','zh-Hans':'次浏览'};
 const show=d=>{views.hidden=!(Number.isInteger(d.views)&&d.views>=0);views.textContent=views.hidden?'':new Intl.NumberFormat(document.documentElement.lang).format(d.views)+' '+(viewLabels[box.dataset.lang]||viewLabels.en);liked=d.liked;button.setAttribute('aria-pressed',String(liked));button.querySelector('[aria-hidden]').textContent=liked?'♥':'♡';button.querySelector('.like-count').textContent=new Intl.NumberFormat(document.documentElement.lang).format(d.likes);};
 const send=async(action)=>{const r=await fetch(API,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({key,client,action}),signal:AbortSignal.timeout(8000)});if(!r.ok)throw new Error('stats unavailable');return r.json();};
 button.addEventListener('click',async()=>{button.disabled=true;try{show(await send(liked?'unlike':'like'));status.textContent=liked?text.liked:text.unliked;}catch{status.textContent=text.failed;}finally{button.disabled=false;}});
 // Do not count prerenders, background tabs, automation, or privacy opt-outs.
 const privateMode=navigator.doNotTrack==='1'||navigator.globalPrivacyControl===true||navigator.webdriver;
 let initialised=false;
 const init=async()=>{if(initialised||document.visibilityState!=='visible')return;initialised=true;try{let d;if(privateMode){const r=await fetch(API+'?key='+encodeURIComponent(key)+'&client='+client,{signal:AbortSignal.timeout(8000)});if(!r.ok)throw new Error();d=await r.json();}else d=await send('view');show(d);button.disabled=false;}catch{status.textContent=text.failed;}};
 document.addEventListener('visibilitychange',init);init();
})();
