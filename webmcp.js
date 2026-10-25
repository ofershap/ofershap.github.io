/* WebMCP (developer.chrome.com/docs/ai/webmcp, webmachinelearning.github.io/webmcp):
   expose blog tools to in-browser AI agents via the Imperative API
   (document.modelContext.registerTool). Feature-detected; a no-op in
   browsers without WebMCP support. */
(function(){
  if(!('modelContext' in document)||typeof document.modelContext.registerTool!=='function')return;
  var BASE='https://ofershap.github.io';
  function searchPosts(args){
    var q=(args&&args.query||'').toLowerCase();
    return fetch(BASE+'/llms.txt').then(function(r){return r.text();}).then(function(t){
      var matches=t.split('\n').filter(function(l){return l.indexOf('](')>-1&&(!q||l.toLowerCase().indexOf(q)>-1);}).slice(0,10);
      return {results:matches,source:BASE+'/llms.txt'};
    });
  }
  try{
    document.modelContext.registerTool({
      name:'search_posts',
      description:"Search Ofer Shapira's blog posts and guides by topic (Hebrew and English).",
      inputSchema:{type:'object',properties:{query:{type:'string',description:'Topic or keywords to look for'}},required:['query']},
      annotations:{readOnlyHint:true},
      execute:searchPosts
    });
  }catch(e){/* WebMCP unavailable or registration rejected: stay silent */}
})();
