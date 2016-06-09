Required packages:

python 2.7.11
pandas
numpy
os.path2

###############################
python GetCenters.py
	#get list of centers of census tracts (FID,xcnt,ycnt)
	#future develop into get list of centers of census tracts within 1 miles ... 
	#...[FID1,FID1_dist,FID2_dist, ... , FIDN_dist;FID2,FID1_dist,FID2_dist, ... , FIDN_dist;...] 
	#input files "./Data/centerlist.csv" (export from shapefiles from ArcGIS)
	#output files "./Output/nearlist.csv"