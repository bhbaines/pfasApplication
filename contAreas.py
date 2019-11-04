import grass.script as grass


#Snap Coordinates

#Add attribute table, join, drop uneeded columns, and export to csv

#C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\gps_sites_snapped_table.csv
snapped_pts = 'C:/bhbaines_Capstone/data/gps_sites_snapped_table.csv'
usgsDir = 'C:/bhbaines_Capstone/scratch'

sites_file = open(snapped_pts, 'r')
sites = sites_file.readlines()[1:]
sites_cleaned = [site.strip() for site in sites]
coords = [site.split(',') for site in sites_cleaned]


#Create cont areas using 500m DEM and snapped points csv as outlet points, convert areas to vectors, download usgs NED data for this area
for site in coords:
    cat = int(site[0].strip('"'))
    coordPair = '{},{}'.format(site[1],site[2])
    grass.run_command('g.region', raster='elev_state_500m_dir')
    grass.run_command('r.water.outlet', input='elev_state_500m_dir',output='ContArea_{}'.format(cat), 
                      coordinates=coordPair, overwrite=True)
    grass.run_command('r.to.vect', input='ContArea_{}'.format(cat), output='ContArea_{}_vect'.format(cat), type='area', overwrite=True)
    grass.run_command('g.region', vector='ContArea_{}_vect'.format(cat))

#Patch all usgs raster together
    




