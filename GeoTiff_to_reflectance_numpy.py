import matplotlib.pyplot as plt
import numpy as np
import tifffile
import math
import gc

X = '173020_20180625_20180704'

folder = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X+'_01_T1_B'
folder2 = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X+'_01_T1_MTL.txt'

data={}

with open(folder2) as file:
    for line in file:
        key, *value = line.split()
        data[key] = value
        
SUN_ELEVATION = float(data['SUN_ELEVATION'][1])
SUN_ELEVATION_Rad = SUN_ELEVATION*math.pi/180
EARTH_SUN_DISTANCE  = float(data['EARTH_SUN_DISTANCE'][1])

for  i in range(7):
    image = tifffile.imread(folder + str(i+1)+'.tif', key=0)
    DN = np.array(image)
    
    RADIANCE_MAXIMUM_BAND = float(data['RADIANCE_MAXIMUM_BAND_'+str(i+1)][1])
    REFLECTANCE_MAXIMUM_BAND = float(data['REFLECTANCE_MAXIMUM_BAND_'+str(i+1)][1])
    RADIANCE_MULT_BAND = float(data['RADIANCE_MULT_BAND_'+str(i+1)][1])
    RADIANCE_ADD_BAND = float(data['RADIANCE_ADD_BAND_'+str(i+1)][1])
    
    Radiance = DN * RADIANCE_MULT_BAND + RADIANCE_ADD_BAND
    Sun_radiance = ((math.pi*EARTH_SUN_DISTANCE**2)**2*RADIANCE_MAXIMUM_BAND*np.sin(SUN_ELEVATION_Rad))/REFLECTANCE_MAXIMUM_BAND
    Reflectance = Radiance/Sun_radiance
    
    b = np.array(Reflectance,dtype = np.float32)
    np.save('Landsat_'+ X +'_B' + str(i+1), b)
    
    plt.title("Band "+str(i+1))
    plt.imshow(Reflectance,cmap = "gray")
    plt.show()
    
    Reflectance = None
    gc.collect()
    b = None
    gc.collect()
    
