# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:55:51 2020

@author: Катя
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:07:03 2019

@author: Alexandra
"""

import math
import tifffile
import numpy as np
import matplotlib.pyplot as plt


def Temperature(n, K2_CONSTANT_BAND, K1_CONSTANT_BAND):
    TKelvin = K2_CONSTANT_BAND / math.log(K1_CONSTANT_BAND/n +1 )
    TCelsium = TKelvin - 273.15
    return TCelsium

def DNtoTCelsium(filepath, info, n_band, resultfolder):
    band = filepath + '_01_T1_B' + str(n_band) +'.tif'
    mtl  = filepath + '_01_T1_MTL.txt'

    
    # Open the file:
    image = tifffile.imread(band, key=0)
    Band = np.array(image)

    data={}
    
    with open(mtl) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
    
    
    RADIANCE_MULT_BAND = float(data['RADIANCE_MULT_BAND_'+str(n_band)][1])
    RADIANCE_ADD_BAND = float(data['RADIANCE_ADD_BAND_'+str(n_band)][1])
    K2_CONSTANT_BAND = float(data['K2_CONSTANT_BAND_'+str(n_band)][1])
    K1_CONSTANT_BAND = float(data['K1_CONSTANT_BAND_'+str(n_band)][1])
    
    TOARadiance = RADIANCE_MULT_BAND * Band + RADIANCE_ADD_BAND
    
    shape = TOARadiance.shape
    Band_T = np.zeros(shape)
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            Band_T[i][j] = Temperature(TOARadiance[i][j],K2_CONSTANT_BAND,K1_CONSTANT_BAND)
    
    print(np.max(Band_T), ' Max Temperature')
    
    
    Band_T_float32 = np.array(Band_T, dtype = np.float32)
    
    np.save(resultfolder + 'Temperature_Band_' + str(n_band) +'_'+info, Band_T_float32 )
    print('Temperature_Band_' + str(n_band) +'_'+info + ' done')



