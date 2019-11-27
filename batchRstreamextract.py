import sys
import grass.script as gs
import os
import re

# all: ^ContArea.+accum$

if len(sys.argv) != 1 and sys.argv[1]:
    pattern = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2]:
        elevRast = sys.argv[2]
        if len(sys.argv) > 3 and sys.argv[3]:
            streamThresh = float(sys.argv[3])
            if len(sys.argv) == 5 and sys.argv[4]:
                exclude = sys.argv[4]
            else:
                exclude = None
        else:
            sys.exit("Missing Stream Threshold value - Usage: script.py pattern streamThresh (e.g., 25000)")
    else:
        sys.exit("Please enter name of elevation raster - Usage: script.py pattern elevation")
else:
    sys.exit("Please enter filename pattern - Usage: script.py pattern (e.g., ^ContArea_SW_[0-9]+_vect$)")

accumRasts = gs.read_command("g.list", type="raster", pattern=pattern, exclude=exclude, flags="e", mapset=".").splitlines()

gs.use_temp_region()

print("Processing {} raster maps...".format(len(accumRasts)))

for accum in accumRasts:
    gs.run_command("g.region", raster=accum)

    try:
        gs.run_command("r.stream.extract", accumulation=accum, elevation=elevRast, threshold=streamThresh, stream_raster=accum + '_streams', memory=131072)
    except gs.CalledModuleError:
        print("Failed computing:", accum)
        raise
