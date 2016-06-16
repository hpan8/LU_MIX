#!/usr/bin/env python
import pandas as pd
import numpy as np
import math
import pprint
import os

OUTPUT = "./Output/Weighted_Entropy.csv"
CUTOFF = 100

#Calculate GWR and Weighted Entropy
GIS_DATA = "./Data/centerlist.csv"

class WeightedEntropy():
    def __init__(self, cutoff = CUTOFF,
                 fname = GIS_DATA, output = OUTPUT):
        # read data
        self.input_data = pd.read_csv(fname)
        siz = len(self.input_data.loc[:, "FID"])
        self.output = OUTPUT
        self.cutoff = cutoff

        #initiliaze parameters
        self.input_weight = []
        self.wtd_lu = []
        self.weights = []
        self.out_ent = np.empty((siz, 2), float)
        colnames = ['FID', 'ent']
        self.out_ent = pd.DataFrame(self.out_ent, columns = colnames)
        self.crnt_ind = 0
        self.getent(self.input_data, self.out_ent, output, cutoff)

    #calculate entropy by weighted land_use
    def getent(self, input_data, out_ent, output, cutoff):
        matrix = input_data
        for i in matrix.loc[:, "FID"]:
        #for i in range(992):
            self.crnt_ind = i
            self.wtd_lu = self.get_w_lu(self.crnt_ind, input_data, cutoff)
            tot = np.sum(self.wtd_lu)
            #print "tot=%s." %tot
            frac = self.wtd_lu/tot
            n_lu = np.count_nonzero(frac)
            frac[frac == 0] = 0.01
            #print frac
            e_frac = [frac * np.log(frac)]
            e_frac = np.sum(e_frac)
            e_frac = -1 * e_frac / math.log(n_lu)
            ent = [i, np.sum(e_frac)]
            print i
            print len(matrix.loc[:, "FID"])
            if np.isnan(ent)[1] == True:
                self.out_ent.loc[i, :] = [i,0]
            elif np.isinf(ent)[1] == True:
                self.out_ent.loc[i, :] = [i, 0]
            else:
                self.out_ent.loc[i, :] = ent
            #print self.out_ent
            print ent
        self.writeoutput(out_ent, output)

    def  get_w_lu(self, crnt_ind, input_data, cutoff):
        matrix = input_data.loc[:, ["E5_RET10", "E5_OFF10", "E5_IND10", "E5_SVC10", "E5_ENT10"]]
        weights = self.getdist(crnt_ind, input_data, cutoff)
        in_lu = matrix.loc[weights.loc[:, "FID"], :]
        in_lu = pd.DataFrame(in_lu, columns=in_lu.columns)
        in_lu = in_lu.reset_index(drop=True)
        add_lu = np.empty((len(weights.loc[:, "FID"]), len(in_lu.loc[0, :])), float)
        add_lu = pd.DataFrame(add_lu, columns = in_lu.columns)
        k = 0
        for i in in_lu.columns:
            a = in_lu.loc[:, i] * weights.loc[:, "wgt"]
            add_lu.loc[:, i] = a
        add_lu = add_lu.sum(axis = 0)
        return add_lu

    def getdist(self, crnt_ind, input_data, cutoff):
        matrix = input_data
        cnt = matrix.loc[crnt_ind, ["xcnt", "ycnt"]]
        dist_array_1 = np.array((matrix.loc[:, "xcnt"] - cnt["xcnt"]) ** 2)
        dist_array_2 = np.array((matrix.loc[:, "ycnt"] - cnt["ycnt"]) ** 2)
        dist_array = np.add(dist_array_1, dist_array_2)
        FID_array = matrix.loc[:, "FID"]
        ind_array = np.where(dist_array < cutoff)
        FID_array = FID_array.loc[ind_array]
        dist_array = dist_array[dist_array < cutoff]
        dist_array = np.sqrt(dist_array)
        dist_array = -0.5 * ((dist_array/cutoff) ** 2)
        dist_array = np.exp(dist_array)
        dist_array = pd.Series(dist_array, name = 'wgt', index = range(len(dist_array)))
        FID_array = pd.Series(FID_array, name = 'FID')
        FID_array = FID_array.reset_index(drop = True)
        dist_array = pd.concat([FID_array, dist_array], axis = 1)
        #print dist_array
        return dist_array

    def writeoutput(self, out_ent, output):
        out_ent.to_csv(output, header=False, index=False)

def main():
        WeightedEntropy()

if __name__ == "__main__":
        main()

