from pathlib import Path
import re

def luminance(h):
 c=[int(h[i:i+2],16)/255 for i in(0,2,4)];c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c];return sum(x*y for x,y in zip(c,[.2126,.7152,.0722]))
bg=luminance('fdfdfb');css=Path('style.css').read_text();assert '#767676' not in css
ratio=(bg+.05)/(luminance('707070')+.05);assert ratio>=4.5,ratio
trial=Path('research/seo-feedback-trial-2026-10-30.md').read_text();assert 'ranking claim' in trial and 'Rollback' in trial
print('PASS evidence trial and muted text contrast:',round(ratio,3))
