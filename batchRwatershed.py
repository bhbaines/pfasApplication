import sys
import grass.script as grass
import os
import re

vectDir = sys.argv[1] #Directory with contributing area vectors
vectFiles = os.listdir(vectDir)
rExternal = sys.argv[2] #name of external raster

pattern = re.compile('Cont.') #Could make text pattern an input
contAreas = [filename for filename in vectFiles if re.match(pattern, filename)]

for area in contAreas:
    grass.run_command(g.region vector=area)
    grass.run_command(r.watershed elevation=rExternal, accumulation=area[:-4] + 'accum', drainage=area[:-4] + 'draindir')


