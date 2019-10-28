import grass.script as grass
import re
import os

vectDir='C:/GRASSdata/GIS_DataBase/nc_spm_08/pfas_02/vector'
usgsDir='//tsclient/D/SanDiskSecureAccess/19arcsecUSGS_DEM_NC'

vects = os.listdir(vectDir)
pattern = re.compile('Cont.')
matches = [filename for filename in vects if re.match(pattern, filename)]

for file in matches:
    grass.run_command('g.region', vector=file)
    grass.run_command('r.in.usgs', product='ned', output_name=file + '19arcsecNED', 
                      output_directory= usgsDir, ned_dataset='ned19sec', flags='k', overwrite=True)

    


