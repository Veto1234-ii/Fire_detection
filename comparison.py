# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:56:21 2020

@author: Катя
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:36:20 2020

@author: Катя
"""
import math
import numpy as np
import gc

    
def Celsius_to_radians(x):
    R = (x * math.pi)/180
    return R
def Count_points(result):

    shape = result.shape
    arr = np.zeros(shape, dtype = np.uint8)
    np.putmask(arr, result!=0, 1)
    return np.sum(arr)

def Lists_coordinates(GT_latarr, GT_lonarr, test_latarr, test_lonarr):
    
    GT_shape = GT_latarr.shape
    print(GT_shape[0], 'Length list coordinates Ground truth')
    test_shape = test_latarr.shape
    print(test_shape[0], 'Length list coordinates test sample')
    
    GT_coord = []
    Test_sample_coord = []
    
    for i in range(GT_shape[0]):
        GT_coord.append((GT_latarr[i], GT_lonarr[i]))
    
    for j in range(test_shape[0]):
        Test_sample_coord.append((test_latarr[j], test_lonarr[j]))
    
    return (GT_coord, Test_sample_coord)

def compare_coordinates_lists(GT_coord, Test_sample_coord):
# Длина меридиана постоянна и равна 20004274 м, 20004274/180 = 111134.86 м  в одном градусе широты, 
# 111134.86/60 = 1852.25 м в одной минуте широты,
# 1852.25/60 = 30.87 м в одной секунде широты
# Длина параллелей не постоянна,  ее можно рассчитать, умножив длину экватора на косинус угла, равного широте.
# Длина экватора = 40000 км
    
    # E_lat = 0.02
    # E_lon = 0.02
    
    E_lat = 30/111134.86
    
    C3 = 0
    
    latarr_Gr3 = []
    lonarr_Gr3 = []
    
    for i in range(len(GT_coord)):
        Len = 40000 * math.cos(Celsius_to_radians(GT_coord[i][0]))# Длина параллели в км
        Degrees = (Len/360)*1000# м в одном градусе долготы
        E_lon = 30/Degrees # сколько градусов долготы в 30 м
        for j in range(len(Test_sample_coord)):
            if abs(GT_coord[i][0] - Test_sample_coord[j][0]) <= E_lat and abs(GT_coord[i][1] - Test_sample_coord[j][1]) <=E_lon:
                C3+=1
                latarr_Gr3.append(GT_coord[i][0])
                lonarr_Gr3.append(GT_coord[i][1])
                
    latarr_Gr3 = np.array(latarr_Gr3)
    lonarr_Gr3 = np.array(lonarr_Gr3)
    
    return (C3, latarr_Gr3, lonarr_Gr3)
          


def compare_masks(ground_truth, test_sample):
    shape = ground_truth.shape
        
    arr = np.abs(ground_truth - test_sample)
        
    Gr3 =  np.zeros(shape, dtype = np.uint8)
    np.putmask(Gr3, np.logical_and(arr == 0, np.logical_and(ground_truth!=0, test_sample!=0)), 1)
    
    S3 = np.sum(Gr3)# точки, которые есть и в эталоне и в тестовых данных
    
    return S3

def Print_group(C3, F3, LenGT_coord, LenTest_sample_coord, Points_GT, Points_test_sample):
    
    C1 = LenGT_coord - C3
    C2 = LenTest_sample_coord - C3
    print(C1,' Points Group1 coordinates')# есть в эталон, нет в тестовых данных. Точки эталона, которые не совпали с тестовыми данными
    print(C2,' Points Group2 coordinates')# есть в тестовых данных, нет в эталоне. Точки тестовых данных, которые не совпали с эталоном
    print(C3,' Points Group3 coordinates')# точки, которые есть и в эталоне и в тестовых данных
    print(Points_test_sample, 'Points_test_sample')
    F1 = Points_GT - F3 
    F2 = Points_test_sample - F3 
    print(F1,' Pixels Group1 firemask')# есть в эталоне, нет в тестовых данных. Пиксели эталона, которые не совпали с тестовыми данными
    print(F2,' Pixels Group2 firemask')# есть в тестовых данных, нет в эталоне. Пиксели тестовых данных, которые не совпали с эталоном
    print(F3,' Pixels Group3 firemask')# Пиксели, которые есть и в эталоне и в тестовых данных


def function(np_folder, info_GT, info_test):

    GT_latarr = np.load( np_folder + r'latarr_'+info_GT+'.npy')
    GT_lonarr = np.load( np_folder + r'lonarr_'+info_GT+'.npy')
    
    test_latarr = np.load( np_folder + r'latarr_'+info_test+'.npy')
    test_lonarr = np.load( np_folder + r'lonarr_'+info_test+'.npy')
    
    firemask1 = np.load(np_folder + r'fire_mask_'+info_test+'.npy')
    firemask2 = np.load(np_folder + r'fire_mask_'+info_GT+'.npy')
    
    Lists = Lists_coordinates(GT_latarr, GT_lonarr, test_latarr, test_lonarr)
    
    List_coord_GT = Lists[0]
    List_coord_Test_sample = Lists[1]
    
    shape_test = test_latarr.shape
    shape_GT = GT_latarr.shape
    
    Points_match = compare_coordinates_lists(List_coord_GT, List_coord_Test_sample)
    C3 = Points_match[0]# Кол-во точек, координаты которых совпали с учетом погрешности
    latarr_Gr3 = Points_match[1]# numpy array, широты точек, которые совпали
    lonarr_Gr3 = Points_match[2]# numpy array, долготы точек, которые совпали
    
    # np.save(np_folder+'latarr_points_math_'+info_GT+'_'+info_test, latarr_Gr3)
    # np.save(np_folder+'lonarr_points_math_'+info_GT+'_'+info_test, lonarr_Gr3)
    
    latarr_Gr3 = None
    lonarr_Gr3 = None
    gc.collect()
    
    Points_GT = Count_points(firemask1)# Кол-во пикселей пожара в firemask1
    Points_test_sample = Count_points(firemask2)# Кол-во пикселей пожара в firemask2
    
    F3 = compare_masks(firemask1, firemask2)# кол-ва пикселей firemasks, которые совпали
    
    Print_group(C3, F3, shape_GT[0], shape_test[0], Points_GT, Points_test_sample)

function('result/', '188034_20140623_20170421', '188034_20140319_20170425')    
    
    
    
    
    
    
    
    
    



