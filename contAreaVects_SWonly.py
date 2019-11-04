import grass.script as grass

#Snap Coordinates

#Add attribute table, join, drop uneeded columns, and export to csv

#C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\gps_sites_snapped_table.csv
snapped_pts = 'C:/NCSU_MGIST_Portofolio_Archive/GIS590/Project/Data/gps_sites_v6_SW_snapped/gps_sites_v6_SW_snapped.csv'


sites_file = open(snapped_pts, 'r')
sites = sites_file.readlines()[1:]
sites_cleaned = [site.strip() for site in sites]
coords = [site.split(',') for site in sites_cleaned]


#Create cont areas using 500m DEM and snapped points csv as outlet points, convert areas to vectors, download usgs NED data for this area
for site in coords:
    epa = int(site[3].strip('"'))
    coordPair = '{},{}'.format(site[1],site[2])
    grass.run_command('g.region', raster='flowAccum_500m')
    grass.run_command('r.water.outlet', input='flowDir_500m',output='ContArea_SW_{}'.format(epa), 
                      coordinates=coordPair, overwrite=True)
    grass.run_command('r.to.vect', input='ContArea_SW_{}'.format(epa), output='ContArea_SW_{}_vect'.format(epa), type='area', overwrite=True)
