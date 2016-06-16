Required packages:  
  
python 2.7.11  
pandas  
numpy  
os.path2  

###############################  
python GetCenters.py  
	#function_1:get list of centers of census tracts (FID,xcnt,ycnt)  
	#output files "./Output/nearlist.csv"   
	#function_2:find tracts within cutoff region and get distance (1 mile in the example)  
	#output files "./Output/dist_mat.txt"  
	#...[FID1,FID1_dist,FID2_dist, ... , FIDN_dist;FID2,FID1_dist,FID2_dist, ... , FIDN_dist;...]   
	#input files "./Data/centerlist.csv" (export from shapefiles from ArcGIS)  

python Weighted_Entropy.py
	#calculate and write weighted entropy for each FID  
	#output files "./Output/WeightedEntropy.csv"   
	#[FID1,weighted_ent;FID2,weighted_ent;...]
	#input files"""./Data/centerlist.csv"  