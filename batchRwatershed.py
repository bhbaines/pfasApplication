import sys
import grass.script as gs
import os
import re

if len(sys.argv) in (3, 4) and sys.argv[1] and sys.argv[2]:
    elevation = sys.argv[1]
    pattern = sys.argv[2]
    if len(sys.argv) == 4:
        exclude = sys.argv[3]
    else:
        exclude = None
else:
    sys.exit("Usage: script.py elevation pattern [exclude]\nExample: %s dem '^ContArea_SW_[0-9]+_vect$'" % sys.argv[0])

contAreas = gs.read_command("g.list", type="vector", pattern=pattern, exclude=exclude, flags="e").splitlines()

gs.use_temp_region()

gs.run_command("g.region", raster=elevation)

for area in contAreas:
    gs.run_command("g.region", vector=area, align=elevation)

    try:
        gs.run_command("r.watershed", elevation=elevation, accumulation=area[:-4] + 'accum', drainage=area[:-4] + 'draindir', memory=131072, flags="m", overwrite=True)
    except gs.CalledModuleError:
        print("Failed computing:", area)
        raise
