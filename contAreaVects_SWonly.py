import grass.script as grass

#Snap Coordinates
#Add attribute table, join, drop uneeded columns, and export to csv
#C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\gps_sites_snapped_table.csv

snapped_pts = sys.argv[1] #full path to csv file output from db.out.ogr for snapped points
drainDir = sys.argv[2] #drainage direction raster

#Open snapped points csv table and read.  Write needed atts into list
sites_file = open(snapped_pts, 'r')
sites = sites_file.readlines()[1:]
sites_cleaned = [site.strip() for site in sites]
coords = [site.split(',') for site in sites_cleaned]





#Create cont areas using drainge direction raster and snapped points csv 
#as outlet points, convert areas to vectors, add column in new vector for epa id and populate
#add this vector to list to be used as input to patching vectors in next step
contAreavects=[]
for site in coords:
    epa = int(site[3].strip('"'))
    coordPair = '{},{}'.format(site[1],site[2])
    contArearast='ContArea_SW_{}'.format(epa)
    contAreavect='ContArea_SW_{}_vect'.format(epa)
    #batch GRASS commands
    grass.run_command('g.region', raster=drainDir)
    grass.run_command('r.water.outlet', input=drainDir, output=contArearast, 
                      coordinates=coordPair, overwrite=True)
    grass.run_command('r.to.vect', input=contArearast, output=contAreavect, type='area', overwrite=True)
    grass.run_command('v.db.addcolumn', map=contAreavect, columns='epa_src_id integer')
    grass.run_command('v.db.update', map=contAreavect, layer='1', column='epa_src_id', value=epa)
    contAreavects.append(contAreavect)
#Patch contributing area vectors

grass.run_command('v.patch', input=contAreavects, output=contAreas_merged, flags ='e')
