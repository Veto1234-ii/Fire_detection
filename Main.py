# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 07:31:59 2020

@author: Alexandra
"""
from GeoTiff_to_reflectance_numpy_2 import DNtoReflectance
from Mask_true_false_borders import calculateBorders
from Algorithm import detectFire
from coordinates import FromMaskToCoords

# X = '135018_20180615_20180703'
# filepath = r'J:\GIS_DATA\Fire\2018\LC08_L1TP_'+X+'_01_T1\LC08_L1TP_' + X

X = '176022_20181020_20181031'
filepath = r'F:\Gis\176022\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X

for i in range(1,8):
    DNtoReflectance(filepath, X, i, "result/")
 
# вырубили   
#calculateBorders(filepath, "result/", X, "result/", 40)

detectFire("result/", X)

mtl = filepath + '_01_T1_MTL.txt'
firemask = r'result\fire_mask_'+X+'.npy'

FromMaskToCoords(filepath, "result/", X, firemask)