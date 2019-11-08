import sys
import grass.script as gs
import os
import re

# all: ^ContArea_SW_[0-9]+_vect$

if len(sys.argv) != 1 and sys.argv[1]:
    pattern = sys.argv[1]
else:
    sys.exit("Usage: script.py pattern (e.g., ^ContArea_SW_[0-9]+_vect$)")

contAreas = gs.read_command("g.list", type="vector", pattern="^ContArea_SW_[0-9]+_vect$", flags="e", mapset=".").splitlines()

for area in contAreas:
    gs.run_command("g.region", vector=area)
    gs.run_command("r.watershed", elevation="ned_19arc", accumulation=area[:-4] + 'accum', drainage=area[:-4] + 'draindir')


