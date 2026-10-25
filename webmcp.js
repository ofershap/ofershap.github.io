/* WebMCP (developer.chrome.com/docs/ai/webmcp, webmachinelearning.github.io/webmcp):
   expose blog tools to in-browser AI agents via the Imperative API
   (document.modelContext.registerTool). Feature-detected; a no-op in
   browsers without WebMCP support. */
(function(){
  if(!('modelContext' in document)||typeof document.modelContext.registerTool!=='function')return;
  var BASE='https://ofershap.github.io';
  function norm(s){return s.normalize('NFKC').toLocaleLowerCase();}
  /* On pages with the visible "Find a post" list, run the same client-side
     search the UI runs (same items, same normalization). Elsewhere, fall back
     to the llms.txt index. */
  function searchDom(q){
    var list=document.querySelector('.post-list');
    if(!list)return null;
    var words=norm(q).split(/\s+/).filter(Boolean);
    var items=[].slice.call(list.querySelectorAll('li:not(.year-group)'));
    var matches=items.filter(function(p){return words.every(function(w){return norm(p.textContent).indexOf(w)>-1;});}).slice(0,10);
    return {results:matches.map(function(p){var a=p.querySelector('a.post-title');return a?{title:a.textContent,url:new URL(a.getAttribute('href'),BASE).href}:null;}).filter(Boolean),source:location.href};
  }
  function searchLlms(q){
    return fetch(BASE+'/llms.txt').then(function(r){return r.text();}).then(function(t){
      var matches=t.split('\n').filter(function(l){return l.indexOf('](')>-1&&(!q||l.toLowerCase().indexOf(q)>-1);}).slice(0,10);
      return {results:matches,source:BASE+'/llms.txt'};
    });
  }
  function searchPosts(args){
    var q=(args&&args.query||'');
    var dom=searchDom(q);
    if(dom)return Promise.resolve(dom);
    return searchLlms(q.toLowerCase());
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
