import unittest,json,re,hashlib,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class Engagement(unittest.TestCase):
 def test_pages_and_no_private_counts(self):
  pages=list(ROOT.glob('posts/*/index.html'))+list(ROOT.glob('essays/*/index.html'))
  for lang in ['en','ar','es','zh-Hans']:pages+=list(ROOT.glob(lang+'/posts/*/index.html'))
  pages=[p for p in pages if 'data-authored="qa"' not in p.read_text()]
  self.assertEqual(len(pages),len(set(pages)))
  source=json.loads((ROOT/'archive-source.json').read_text())
  expected={ROOT/'posts'/('linkedin-'+r['id'])/'index.html' for r in source if not r.get('existing') and r.get('text','').strip()}
  self.assertTrue(expected.issubset(set(pages)),expected-set(pages))
  for p in pages:
   s=p.read_text()
   if 'data-engagement="off"' in s:self.assertEqual(s.count('<!-- engagement:start -->'),0,str(p));continue
   self.assertEqual(s.count('<!-- engagement:start -->'),1,str(p));self.assertEqual(s.count('src="/engagement-v2.js"'),1,str(p));self.assertNotIn('ADMIN_TOKEN',s);self.assertNotIn('data-views',s)
 def test_rebuild_idempotence(self):
  import tempfile,shutil
  with tempfile.TemporaryDirectory() as tmp:
   work=Path(tmp)/'site';shutil.copytree(ROOT,work,ignore=shutil.ignore_patterns('.git','__pycache__'))
   files=list(work.glob('posts/*/index.html'))+list(work.glob('essays/*/index.html'))
   before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
   subprocess.run(['python3','build_engagement.py'],cwd=work,check=True,stdout=subprocess.DEVNULL)
   self.assertEqual(before,{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
 def test_privacy_and_backend(self):
  s=(ROOT/'engagement-backend/worker.js').read_text();self.assertIn('new_sqlite_classes',(ROOT/'engagement-backend/wrangler.jsonc').read_text());self.assertIn('unauthorised',s);self.assertIn('origin not allowed',s);self.assertIn('views=views+1',s);self.assertIn('e.viewed!==day',s)
  front=(ROOT/'engagement-v2.js').read_text();self.assertIn('globalPrivacyControl',front);self.assertIn('navigator.webdriver',front);self.assertIn('visibilityState',front);self.assertNotIn('/admin/stats',front)
if __name__=='__main__':unittest.main()
