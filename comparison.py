# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:08:51 2020

@author: Катя
"""
import math
import numpy as np
import gc
import matplotlib.pyplot as plt
from Visualization_result_matplot import Visualization_nparray_coordinates, Visualization_arr
from utilities import getMTL

def Minimum_Len_array(arr1, arr2):
    
    if len(arr1) < len(arr2):
        GT_coord = arr1
        Test_sample_coord = arr2
    else:
        GT_coord = arr2
        Test_sample_coord = arr1
        
    return (GT_coord, Test_sample_coord)

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

def Minimum_distance(arr1, arr2):
    
    arrays = Minimum_Len_array(arr1, arr2)
    GT_coord = arrays[0]
    Test_sample_coord = arrays[1]
    
    arr_minimum = []     

    for i in range(len(GT_coord)):
        arr = []
        for j in range(len(Test_sample_coord)):
            
            diff_lat = abs(GT_coord[i][0] - Test_sample_coord[j][0])
            diff_lon = abs(GT_coord[i][1] - Test_sample_coord[j][1])
            
            diff = (diff_lat**2 + diff_lon**2)**0.5
            arr.append(diff)
            
        arr_minimum.append(min(arr))
        

    return min(arr_minimum)

def Сalculation_E_diff_corners(filepath, np_filepath, info):
    
    b1 = np.load(np_filepath + r'Landsat_' + info + '_B1.npy')
    mtl  = filepath + '_01_T1_MTL.txt'
    data = getMTL(mtl)

    UL_LAT = float(data['CORNER_UL_LAT_PRODUCT'])
    UL_LON = float(data['CORNER_UL_LON_PRODUCT'])
    UR_LAT = float(data['CORNER_UR_LAT_PRODUCT'])
    UR_LON = float(data['CORNER_UR_LON_PRODUCT'])
    LL_LAT = float(data['CORNER_LL_LAT_PRODUCT'])
    LL_LON = float(data['CORNER_LL_LON_PRODUCT'])
    LR_LAT = float(data['CORNER_LR_LAT_PRODUCT'])
    LR_LON = float(data['CORNER_LR_LON_PRODUCT'])
    
    shape = b1.shape
    mask = np.zeros(shape)

    np.putmask(mask,b1!=b1[0][0],1)

    ind_lines = []
    for i in range(shape[0]):
       if np.sum(mask[i,:])<=5 and np.sum(mask[i,:])!=0:
           ind_lines.append(i)

    ind_columns = []
    for j in range(shape[1]):
       if np.sum(mask[:,j])<=5 and np.sum(mask[:,j])!=0:
           ind_columns.append(j)

    Max_ind_line = max(ind_lines)
    Min_ind_line = min(ind_lines)
    Max_ind_col = max(ind_columns)
    Min_ind_col = min(ind_columns)

    offsetX = Min_ind_col
    offsetY = Min_ind_line
    
    Max_Lat = max(UL_LAT,UR_LAT,LL_LAT,LR_LAT)
    Min_lat = min(UL_LAT,UR_LAT,LL_LAT,LR_LAT)
    Max_lon = max(UL_LON,UR_LON,LL_LON,LR_LON)
    Min_lon = min(UL_LON,UR_LON,LL_LON,LR_LON)
    
    p_lat = abs((Max_Lat - Min_lat)/(Max_ind_line - offsetY))
    p_lon = abs((Max_lon - Min_lon)/(Max_ind_col - offsetX))
    
    E_diff = (p_lat**2 + p_lon**2)**0.5
    return  E_diff


def Сalculation_E_diff_compare_coordinates(arr1, arr2):
    
    arrays = Minimum_Len_array(arr1, arr2)
    GT_coord = arrays[0]
    Test_sample_coord = arrays[1]
        
    E_lat = 30/111134.86
    Gr3 = []
    for i in range(len(GT_coord)):
        
        Len = 40000 * math.cos(To_radians(GT_coord[i][0]))
        Degrees = (Len/360)*1000# m in 1 Degree
        E_lon = 30/Degrees 
        E_diff = (E_lat**2 + E_lon**2)**0.5
        arr = []     
        for j in range(len(Test_sample_coord)):
            diff_lat = abs(GT_coord[i][0] - Test_sample_coord[j][0])
            diff_lon = abs(GT_coord[i][1] - Test_sample_coord[j][1])
            
            diff = (diff_lat**2 + diff_lon**2)**0.5
            arr.append(diff)
            
        
        if min(arr) <= E_diff:
            
            Gr3.append((GT_coord[i][0], GT_coord[i][1]))
            
    return Gr3

def compare_coordinates_lists(arr1, arr2, E_diff):
    
    arrays = Minimum_Len_array(arr1, arr2)
    GT_coord = arrays[0]
    Test_sample_coord = arrays[1]
    
    Gr3 = []    
    for i in range(len(GT_coord)):
        arr = []
        for j in range(len(Test_sample_coord)):
            
            diff_lat = abs(GT_coord[i][0] - Test_sample_coord[j][0])
            diff_lon = abs(GT_coord[i][1] - Test_sample_coord[j][1])
            
            diff = (diff_lat**2 + diff_lon**2)**0.5
            arr.append(diff)
            
        if min(arr) <= E_diff:
            Gr3.append((GT_coord[i][0], GT_coord[i][1]))
        

    return Gr3