#!/usr/bin/env python
import pandas as pd
import numpy as np
import math
import pprint
import os

output = "./Output/Weighted_Entropy.csv"


#Calculate GWR and Weighted Entropy
fname = "./Data/centerlist.csv"

class WeightedEntropy():
    def __init__(self, input_Weight, input_LU, Input_Data):
        inputw_Data = read.csv(fname)
