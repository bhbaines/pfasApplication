import sys
import os
import csv


gpsFile = open(sys.argv[1], 'r')  #r'C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\gps_sites_v6.txt'  
chem_tempFile = open(sys.argv[2], 'r')  #r'C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\chem_con_template.txt'
chem_conFile = open(sys.argv[3], 'w')  #r'C:\NCSU_MGIST_Portofolio_Archive\GIS590\Project\Data\chem_con.csv'
chem_conWrite = csv.writer(chem_conFile, delimiter=',', lineterminator='\n')
epa_IDs = []


gpsRead = gpsFile.readlines()[1:]
chemRead = chem_tempFile.readlines()
for row in gpsRead:
    cells = row.split('\t')
    epaID = cells[10]
    epa_IDs.append(epaID)


for id in epa_IDs:
    for row in chemRead:
        cells = row.split('\t')
        cellsCleaned = [cell.strip() for cell in cells]
        cellsCleaned.insert(0,id)
        chem_conWrite.writerow(cellsCleaned)
    



gpsFile.close()
chem_tempFile.close()
chem_conFile.close()
