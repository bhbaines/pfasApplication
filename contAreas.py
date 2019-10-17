#import grass.script as grass
import sys
import os


#C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\gps_sites_snapped_table.csv
snapped_pts = sys.argv[1]

sites_file = open(snapped_pts, 'r')
sites = sites_file.readlines()[1:]
sites_cleaned = [site.strip() for site in sites]
coords = [site.split(',') for site in sites_cleaned]

for site in coords:
    coordPair = '{},{}'.format(site[1],site[2])
    print (coordPair)



