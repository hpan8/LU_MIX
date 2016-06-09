#!/usr/bin/env python
import pandas as pd
import numpy as np
import math
import pprint
import os

output="./Output/nearlist.csv"
directory="./Output"

#get center list with (id,x,y)
def getcenter(fname):
    matrix=pd.read_csv(fname)
    center_list=matrix.loc[:,["FID","xcnt","ycnt"]]
    names=["FID","xcnt","ycnt"]
    center_list = pd.DataFrame(center_list, index=None, columns=names)
    print center_list
    return center_list

def main():
    gis_data = "./Data/centerlist.csv"
    center_list_g=getcenter(gis_data)
    if not os.path.exists(directory):
        os.makedirs(directory)
    center_list_g.to_csv(output,header=True,index=False)

if __name__ == "__main__":
    main()


