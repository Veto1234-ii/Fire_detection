# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:02:08 2020

@author: Катя
"""
import math
import pandas as pd
from utilities import getMTL
import datetime
from comparison import *

X = '026048_20140507_20170306'

filepath = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X
np_filepath = r'result/'

mtl = filepath + '_01_T1_MTL.txt'

# FIRMS = np_filepath + r'fire_archive_M6_120741.csv'
FIRMS = np_filepath + r'fire_archive_M6_120507.csv'


E_diff = 1# км

def Max_Min_Lat_Lon(mtl):
    data =  getMTL(mtl)
    
    UL_LAT = float(data['CORNER_UL_LAT_PRODUCT'])
    UL_LON = float(data['CORNER_UL_LON_PRODUCT'])
    UR_LAT = float(data['CORNER_UR_LAT_PRODUCT'])
    UR_LON = float(data['CORNER_UR_LON_PRODUCT'])
    LL_LAT = float(data['CORNER_LL_LAT_PRODUCT'])
    LL_LON = float(data['CORNER_LL_LON_PRODUCT'])
    LR_LAT = float(data['CORNER_LR_LAT_PRODUCT'])
    LR_LON = float(data['CORNER_LR_LON_PRODUCT'])
    
    Max_lat = max(UL_LAT,UR_LAT,LL_LAT,LR_LAT)
    Min_lat = min(UL_LAT,UR_LAT,LL_LAT,LR_LAT)
    Max_lon = max(UL_LON,UR_LON,LL_LON,LR_LON)
    Min_lon = min(UL_LON,UR_LON,LL_LON,LR_LON)
    return (Max_lat, Min_lat, Max_lon, Min_lon)

def FIRMS_coordinates(FIRMS, mtl, info):
    
    df = pd.read_csv(FIRMS, sep=',')
    
    columns = list(df.columns)
    print(columns)
    print()
    lat_lon = Max_Min_Lat_Lon(mtl)
    
    Max_lat = lat_lon[0]
    Min_lat = lat_lon[1]
    Max_lon = lat_lon[2]
    Min_lon = lat_lon[3]
    
    print(Min_lat, Max_lat, 'latitude snapshot')
    print(Min_lon, Max_lon, 'Longitude snapshot')
    
    z_lat  = (df.latitude >=  Min_lat) & (df.latitude <= Max_lat)
    z_lon  = (df.longitude >=  Min_lon) & (df.longitude <= Max_lon)
    z_coor = z_lat & z_lon
    
    date = str(datetime.date(int(info[7:11]),int(info[11:13]),int(info[13:15])))
    print()
    print(date)
    print()
    df_sort = df[(df.acq_date == date) & (df.daynight == 'D') & z_coor][['latitude', 'longitude','acq_date']]
    print(df_sort)
    print()
    arr_lat = np.array(df_sort['latitude'])
    arr_lon = np.array(df_sort['longitude'])
    arr = []
       
    for i in range(arr_lat.shape[0]):
        arr.append((arr_lat[i], arr_lon[i]))
            
    return arr

GR = FIRMS_coordinates(FIRMS, mtl, X)
Test = Lists_coordinates(np_filepath, X)


func = Сalculation_E_diff_corners(filepath, np_filepath, X)
p_lat = func[0]/30*1000
p_lon = func[1]/30*1000

print(p_lat,'degrees of latitude in 1 kilometer')
print(p_lon,'degrees of longitude in 1 kilometer')
print()

res = compare_coordinates_lists_2(GR, Test, E_diff)
print(res, 'Result')
