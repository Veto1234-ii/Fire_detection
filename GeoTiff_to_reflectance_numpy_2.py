import numpy as np
import tifffile
import math
import gc
from utilities import getMTL

def DNtoReflectance(filepath, info, n_band, resultfolder):
    num_band = str(n_band)
    band = filepath + '_01_T1_B' + num_band +'.tif'
    mtl  = filepath + '_01_T1_MTL.txt'

    data = getMTL(mtl)


    image = tifffile.imread(band, key=0)
    DN = np.array(image)

    
    REFLECTANCE_MULT_BAND =       float(data['REFLECTANCE_MULT_BAND_'       + num_band])
    REFLECTANCE_ADD_BAND =        float(data['REFLECTANCE_ADD_BAND_'        + num_band])

    Reflectance = DN * REFLECTANCE_MULT_BAND + REFLECTANCE_ADD_BAND
    
    print(np.max(Reflectance), ' Max Value Band '+ num_band)
    print(np.min(Reflectance), ' Min Value Band '+ num_band)
    
    b = np.array(Reflectance,dtype = np.float32)
    np.save(resultfolder + 'Landsat_'+ info +'_B' + num_band, b)
    Reflectance = None
    b = None
    gc.collect()
    print("save "+ 'Landsat_'+ info +'_B' + num_band)
