# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:08:51 2020

@author: Катя
"""
import math
import numpy as np
import gc
import matplotlib.pyplot as plt



def To_radians(x):
    R = (x * math.pi)/180
    return R

def Lists_coordinates(np_folder, info):
    
    arr_lat = np.load(np_folder + r'latarr_'+info+'.npy')
    arr_lon = np.load(np_folder + r'lonarr_'+info+'.npy')
    
    arr = []
   
    for i in range(arr_lat.shape[0]):
        arr.append((arr_lat[i], arr_lon[i]))
    
    
    return arr

def compare_coordinates_lists(arr1, arr2):
    
    if len(arr1) < len(arr2):
        GT_coord = arr1
        Test_sample_coord = arr2
    else:
        GT_coord = arr2
        Test_sample_coord = arr1
    
    E_lat = 30/111134.86
    Gr3 = []
    for i in range(len(GT_coord)):
        
        Len = 40000 * math.cos(To_radians(GT_coord[i][0]))
        Degrees = (Len/360)*1000
        E_lon = 30/Degrees 
        E_diff = (E_lat**2 + E_lon**2)**0.5
        arr = []     
        for j in range(len(Test_sample_coord)):
            diff_lat = abs(GT_coord[i][0] - Test_sample_coord[j][0])
            diff_lon = abs(GT_coord[i][1] - Test_sample_coord[j][1])
            
            diff = (diff_lat**2 + diff_lon**2)**0.5
            arr.append(diff)
            
        
        if min(arr) < E_diff:
            # print(min(arr), 'MIN')   
            # print(E_diff, ' E_diff')
            # print()
            Gr3.append((GT_coord[i][0], GT_coord[i][1]))
            
    return Gr3

# arr1 = Lists_coordinates(r'result/points_match/', '20140319')
# arr2 = Lists_coordinates(r'result/points_match/', '20140522')
# res = compare_coordinates_lists(arr1, arr2)

# print(res)
# print(len(res))
# print(len(arr1))
# print(len(arr2))