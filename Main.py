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
from Mask_Image_points import  Save_mask_image_points

def Main(X, filepath, FIRMS, mtl, path_res):
    
    E_diff = 1 # 1 km
    
    
    firemask = path_res + r'\fire_mask_'+X+'.npy'
    
    for i in range(1,8):
        DNtoReflectance(filepath, X, i, mtl, path_res)
     
    k_alg = detectFire(path_res, X)
    FromMaskToCoords(path_res, X, firemask, mtl)
    
    # lat = np.load(path_res + r'\latarr_'+X+'.npy')
    # k_alg = lat.shape[0]

    
    GT   = FIRMS_coordinates(path_res + FIRMS, mtl, X)
    Test = Lists_coordinates(path_res, X)
    
    Points_match = compare_coordinates_lists_2(GT, Test, E_diff)
     
    k_unsure, k_med_conf, k_conf = Grouping_points_confident(Points_match, 40, 60)
    
    Points = len(Points_match)
    
    Save_mask_image_points(firemask, X, path_res)
    
    return k_alg, Points, k_unsure, k_med_conf, k_conf
    
        

    