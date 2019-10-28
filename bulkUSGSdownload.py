import time
import grass.script as grass

#Set output file name and directory
output = 'NC_NED_19arcsecond'
usgsDir = 'D:/SanDiskSecureAccess/19arcsecUSGS_DEM_NC'


restart_after = 0.1 * 3600  # seconds (hours * 60  * 60)
max_tries = 5  # do not try more than n times for one site

#Try downloading n times (n=max_tries)
tries = 0
while tries < max_tries:
        tries += 1
        try:
            grass.run_command('r.in.usgs', product='ned', output_name=output,
                              output_directory= usgsDir, ned_dataset='ned19sec', flags='k', overwrite=True)
            break
        except grass.CalledModuleError:
            time.sleep(restart_after)