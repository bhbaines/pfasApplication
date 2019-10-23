import grass.script as grass
import sys
import time

#Snap Coordinates

#Add attribute table, join, drop uneeded columns, and export to csv

#C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\gps_sites_snapped_table.csv
snapped_pts = 'C:/bhbaines_Capstone/data/gps_sites_snapped_table.csv'
usgsDir = 'C:/bhbaines_Capstone/scratch'

sites_file = open(snapped_pts, 'r')
sites = sites_file.readlines()[1:]
sites_cleaned = [site.strip() for site in sites]
coords = [site.split(',') for site in sites_cleaned]

restart_after = 1 * 3600  # seconds (hours * 60  * 60)
max_tries = 5  # do not try more than n times for one site

#Create cont areas using 500m DEM and snapped points csv as outlet points, convert areas to vectors, download usgs NED data for this area
for site in coords:
    cat = int(site[0].strip('"'))
    coordPair = '{},{}'.format(site[1],site[2])
    grass.run_command('g.region', raster='elev_state_500m_dir')
    grass.run_command('r.water.outlet', input='elev_state_500m_dir',output='ContArea_{}'.format(cat), 
                      coordinates=coordPair, overwrite=True)
    grass.run_command('r.to.vect', input='ContArea_{}'.format(cat), output='ContArea_{}_vect'.format(cat), type='area', overwrite=True)
    grass.run_command('g.region', vector='ContArea_{}_vect'.format(cat))
    tries = 0
    while tries < max_tries:
        tries += 1
        try:
            grass.run_command('r.in.usgs', product='ned', output_name='ContArea_{}_NED'.format(cat),
                              output_directory= usgsDir, ned_dataset='ned19sec', flags='k', overwrite=True)
            break
        except grass.CalledModuleError:
            time.sleep(restart_after)


#Patch all usgs raster together
    




