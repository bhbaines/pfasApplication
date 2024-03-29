import sys
import grass.script as gs
import os
import re

if len(sys.argv) in (5, 6) and sys.argv[1] and sys.argv[2] and sys.argv[3] and sys.argv[4]:
    memory = sys.argv[1]
    elevation = sys.argv[2]
    threshold = sys.argv[3]
    pattern = sys.argv[4]
    if len(sys.argv) == 6:
        exclude = sys.argv[5]
    else:
        exclude = None
else:
    sys.exit("Usage: script.py memory elevation pattern [exclude]\nExample: %s dem '^ContArea_SW_[0-9]+_vect$'" % sys.argv[0])

contAreas = gs.read_command("g.list", type="vector", pattern=pattern, exclude=exclude, flags="e").splitlines()

gs.use_temp_region()

gs.run_command("g.region", raster=elevation)

if memory == "all":
    memory = None
    flags = None
else:
    flags = "m"

print("Processing {} raster maps...".format(len(contAreas)))

for area in contAreas:
    gs.run_command("g.region", vector=area, align=elevation)

    try:
        gs.run_command("r.watershed", elevation=elevation, accumulation=area[:-4] + 'accum', drainage=area[:-4] + 'draindir', stream=area[:-4] + 'stream', threshold=threshold, memory=memory, flags=flags, overwrite=True)
    except gs.CalledModuleError:
        print("Failed computing:", area)
        raise
