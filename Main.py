# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 07:31:59 2020

@author: Alexandra
"""
from GeoTiff_to_reflectance_numpy_2 import DNtoReflectance
from Mask_true_false_borders import calculateBorders
from Algorithm import detectFire
from coordinates import FromMaskToCoords
from comparison import *
from open_sort_csv import FIRMS_coordinates


def Main(X, filepath, FIRMS, mtl):
    
    E_diff = 1 # 1 km
    
    
    firemask = filepath + r"/result/" + 'fire_mask_'+X+'.npy'
    
    for i in range(1,8):
        DNtoReflectance(filepath, X, i, mtl)
     
    k_alg = detectFire(filepath, X)
    FromMaskToCoords(filepath, X, firemask, mtl)
    

    
    GT   = FIRMS_coordinates(filepath + r"/result/" + FIRMS, mtl, X)
    Test = Lists_coordinates(filepath + r"/result/", X)
    
    Points_match = compare_coordinates_lists_2(GT, Test, E_diff)
     
    k_unsure, k_med_conf, k_conf = Grouping_points_confident(Points_match, 40, 60)
    
    Points = k_unsure + k_med_conf + k_conf
    
    
    return k_alg, Points, k_unsure, k_med_conf, k_conf
    
        

    