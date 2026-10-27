#!/usr/bin/env python3
"""Mandatory final consumer for each bounded archive sync, not a site rebuild.
Pass only source IDs actually synced in this run. Exit 1 means partial, no
completion receipt. New proof entries must bind independently decoded/reviewed
original bytes to source post+asset IDs before this command can pass.
"""
from pathlib import Path
import argparse,json,subprocess,sys
ROOT=Path(__file__).resolve().parent

def main():
 p=argparse.ArgumentParser();p.add_argument('--require',nargs='+',required=True);args=p.parse_args()
 # This subprocess is deliberate: any non-zero media gate must stop completion.
 result=subprocess.run([sys.executable,str(ROOT/'audit_archive_media.py'),'--require',*args.require],capture_output=True,text=True)
 if result.returncode:
  sys.stderr.write(result.stdout+result.stderr)
  print('ARCHIVE_SYNC_PARTIAL: media proof gate failed; no completion receipt.',file=sys.stderr)
  return 1
 print(json.dumps({'state':'source-media-proof-passed','source_ids':args.require,'caveat':'Publication and actual live pixel/playback checks remain required before reporting completion.'}))
 return 0
if __name__=='__main__':sys.exit(main())
