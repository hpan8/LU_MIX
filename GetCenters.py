#!/usr/bin/env python
import pandas as pd
import numpy as np
import math
import pprint
import os

output = "./Output/nearlist.csv"
m_output = "./Output/dist_matrix.txt"
directory = "./Output"
CUTOFF = 1

#get center list with (id,x,y)
def getcenter(fname):
    matrix = pd.read_csv(fname)
    center_list = matrix.loc[:,["FID","xcnt","ycnt"]]
    names = ["FID","xcnt","ycnt"]
    center_list = pd.DataFrame(center_list, index=None, columns=names)
    return center_list

#make center matrix for values smaller than cutoff
def getonemile(row, matrix, cutoff):
    cnt_ind = matrix.loc[row,"FID"]
    cnt = matrix.loc[cnt_ind,["xcnt","ycnt"]]
    dist_array_1 = np.array([(matrix.loc[:,"xcnt"]-cnt["xcnt"])**2])
    dist_array_2 = np.array([(matrix.loc[:, "ycnt"] - cnt["ycnt"]) ** 2])
    dist_array = np.add (dist_array_1,dist_array_2)
    FID_array = matrix.loc[:, "FID"]
    ind_array = np.array(dist_array < cutoff)
    ind_array = ind_array[0,:]
    FID_array = FID_array[ind_array]
    dist_array = dist_array[dist_array < cutoff]
    dist_array = np.sqrt(dist_array)
    dist_array = np.c_[dist_array, FID_array]
    print row
    print len(matrix.loc[:,"FID"])
    return dist_array

def main():
    if not os.path.exists(directory):
        os.makedirs(directory)
    gis_data = "./Data/centerlist.csv"
    center_list_g = getcenter(gis_data)

    #write spatial distance matrix
    with open(m_output, 'w') as m:
        for i in center_list_g.loc[:,"FID"]:
        #for i in range(10):
            my_array = getonemile(i,center_list_g,CUTOFF)
            d_array = ""
            i_array = ""
            for x in my_array[:,0]:
                x = math.ceil(x*100)/100
                d_array = str(d_array + str(x)+",")

            for x in my_array[:,1]:
                x = int(x)
                i_array = str(i_array + str(x)+",")

            m.write("FID"+str(i)+ "\n" + i_array + "\n" + "\n" + d_array + "\n" + "\n")
            #m.write("FID"+str(i)+"\n"+str(my_array).strip('[]')+ "\n")

    center_list_g.to_csv(output, header=True, index=False)

if __name__ == "__main__":
    main()


