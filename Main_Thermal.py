# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:59:42 2020

@author: Катя
"""

from GeoTiff_to_Temperature import DNtoTCelsium
from histogram import histogram_calculation
from Threshold_mask_thermal import Thermal_mask
from Thermal_coordinates import FromMaskToCoords
from Thermal_Visualization import Visualization
X = '188034_20140623_20170421'


filepath = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X


DNtoTCelsium(filepath, X, 10, "result/")

Count = 176
N = 500

threshold = histogram_calculation("result/", 10, X, N, Count)

Thermal_mask(threshold, "result/", 10, X)

Thermalmask = r'result/Thermal_mask_'+X+'.npy'

FromMaskToCoords(filepath, "result/", X, 10, Thermalmask)
Visualization("result/",X,10)

