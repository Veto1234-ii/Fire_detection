# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:30:04 2020

@author: Катя
"""

import numpy as np
import math
import gc

def threshold_selection(np_folder, n_band, info, N, Count):
    T = np.load(np_folder + r'Temperature_Band_' + str(n_band) +'_'+info + '.npy')
    hist = histogram_calculation(T, N)
    np.save(np_folder+'Histogram_'+info, hist)    
    print('histogram done')
    
    Number = 0
    
    for i in range(hist.shape[0]-1,-1,-1):
        Number += hist[i]
        if Number >= Count:
            break
    
    threshold = minval + i*step
    print(threshold)
    return threshold

def histogram_calculation(snapshot, N):
    shape = snapshot.shape
    minval = np.min(snapshot)
    maxval = np.max(snapshot)
    step = (maxval - minval)/(N-1)
    print(step)
    hist = np.zeros(N, dtype = np.uint32)
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            t = snapshot[i][j]
            idx = int(round((t - minval)/step))
            hist[idx]+=1
    return hist




