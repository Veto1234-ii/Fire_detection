import numpy as np
import tifffile
import math
import gc

def DNtoReflectance(filepath, info, n_band, resultfolder):
    band = filepath + '_01_T1_B' + str(n_band) +'.tif'
    mtl  = filepath + '_01_T1_MTL.txt'

    data={}
    with open(mtl) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value

    SUN_ELEVATION = float(data['SUN_ELEVATION'][1])
    SUN_ELEVATION_Rad = SUN_ELEVATION*math.pi/180
    EARTH_SUN_DISTANCE  = float(data['EARTH_SUN_DISTANCE'][1])

    image = tifffile.imread(band, key=0)
    DN = np.array(image)

    RADIANCE_MAXIMUM_BAND =    float(data['RADIANCE_MAXIMUM_BAND_'+   str(n_band)][1])
    REFLECTANCE_MAXIMUM_BAND = float(data['REFLECTANCE_MAXIMUM_BAND_'+str(n_band)][1])
    RADIANCE_MULT_BAND =       float(data['RADIANCE_MULT_BAND_'+      str(n_band)][1])
    RADIANCE_ADD_BAND =        float(data['RADIANCE_ADD_BAND_'+       str(n_band)][1])

    Radiance = DN * RADIANCE_MULT_BAND + RADIANCE_ADD_BAND
    Sun_radiance = ((math.pi*EARTH_SUN_DISTANCE**2)**2*RADIANCE_MAXIMUM_BAND*np.sin(SUN_ELEVATION_Rad))/REFLECTANCE_MAXIMUM_BAND
    Reflectance = Radiance/Sun_radiance

    b = np.array(Reflectance,dtype = np.float32)
    np.save(resultfolder + 'Landsat_'+ info +'_B' + str(n_band), b)
    Reflectance = None
    gc.collect()
    b = None
    gc.collect()
    print("save "+ 'Landsat_'+ info +'_B' + str(n_band))
