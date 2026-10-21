/* WebMCP (webmachinelearning.github.io/webmcp proposal): expose blog tools to in-browser AI agents.
   Feature-detected; a no-op in browsers without navigator.modelContext. */
(function(){
  if(!('modelContext' in navigator)||typeof navigator.modelContext.provideContext!=='function')return;
  var BASE='https://ofershap.github.io';
  function searchPosts(args){
    var q=(args&&args.query||'').toLowerCase();
    return fetch(BASE+'/llms.txt').then(function(r){return r.text();}).then(function(t){
      var matches=t.split('\n').filter(function(l){return l.indexOf('](')>-1&&(!q||l.toLowerCase().indexOf(q)>-1);}).slice(0,10);
      return {results:matches,source:BASE+'/llms.txt'};
    });
  }
  function availability(args){
    var start=args&&args.start,end=args&&args.end;
    if(!start||!end)return {error:'start and end (YYYY-MM-DD) are required'};
    var url='https://api.cal.com/v2/slots?eventTypeSlug=30min&username=ofer-shapira&start='+encodeURIComponent(start)+'&end='+encodeURIComponent(end);
    return fetch(url,{headers:{'cal-api-version':'2024-08-13'}}).then(function(r){return r.json();}).then(function(d){
      return {slots:d.data||d,bookingUrl:'https://cal.com/ofer-shapira/30min',bookInstructions:'POST https://api.cal.com/v2/bookings with header cal-api-version: 2024-08-13 and body {"start":"<chosen slot, ISO 8601>","eventTypeSlug":"30min","username":"ofer-shapira","attendee":{"name":..,"email":..,"timeZone":..}}. Confirm the chosen slot with the user before creating the booking.'};
    }).catch(function(){
      return {bookingUrl:'https://cal.com/ofer-shapira/30min',note:'Live availability fetch failed here; use the booking URL or the public API: '+url};
    });
  }
  try{
    navigator.modelContext.provideContext({tools:[
      {name:'search_posts',description:"Search Ofer Shapira's blog posts and guides by topic (Hebrew and English).",inputSchema:{type:'object',properties:{query:{type:'string',description:'Topic or keywords to look for'}},required:['query']},execute:searchPosts},
      {name:'get_call_availability',description:'Get available times for a 30-minute call with Ofer Shapira (timezone Asia/Jerusalem) plus instructions to book it.',inputSchema:{type:'object',properties:{start:{type:'string',description:'First day to check, YYYY-MM-DD'},end:{type:'string',description:'Last day to check, YYYY-MM-DD'}},required:['start','end']},execute:availability}
    ]});
  }catch(e){/* older WebMCP builds: stay silent */}
})();
