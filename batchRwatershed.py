import sys
#import grass.script as grass
import os
import re

vectDir = sys.argv[1] #C:/NCSU_MGIST_Portofolio_Archive/GIS582/GRASSData/nc_spm_08_grass7/pfas_02/vector
vectFiles = os.listdir(vectDir)

pattern = re.compile('Cont.')
contAreas = [filename for filename in vectFiles if re.match(pattern, filename)]

for area in contAreas:
    grass.run_command(g.region vector=area)
    grass.run_command(r.watershed )
