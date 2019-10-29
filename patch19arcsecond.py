import grass.script as grass
import re
import os
import time

#Set vector directory and directory with USGS data
vectDir='C:/GRASSdata/GIS_DataBase/nc_spm_08/pfas_02/vector'
usgsDir='//tsclient/D/SanDiskSecureAccess/19arcsecUSGS_DEM_NC'

vects = os.listdir(vectDir) #GRASS vector directory
pattern = re.compile('.NED')
contAreas = [filename for filename in vects if not re.match(pattern, filename)]

restart_after = 0.025 * 3600  # seconds (hours * 60  * 60)
max_tries = 10  # do not try more than n times for one site

#Try downloading n times (n=max_tries)
tries = 0
while tries < max_tries:
        tries += 1
        try:
            for file in contAreas:
                grass.run_command('g.region', vector=file)
                grass.run_command('r.in.usgs', product='ned', output_name=file + '19arcsecNED', 
                      output_directory= usgsDir, ned_dataset='ned19sec', flags='k', overwrite=True)
                grass.run_command('g.remove', type='raster', name=file, flags='f')
            break
        except grass.CalledModuleError:
            time.sleep(restart_after)
    


