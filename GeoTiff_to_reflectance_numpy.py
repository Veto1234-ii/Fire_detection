import numpy as np
import tifffile

def DNtoReflectance(filepath, info, n_band, resultfolder):
    band = filepath + '_01_T1_B' + str(n_band) +'.tif'
    mtl  = filepath + '_01_T1_MTL.txt'
    
    data={}
    with open(mtl) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
             
    image = tifffile.imread(band, key=0)
    arr = np.array(image)
    Mult = float(data['REFLECTANCE_MULT_BAND_' + str(n_band)][1])
    Add =  float(data['REFLECTANCE_ADD_BAND_'  + str(n_band)][1])
    arr_reflectance = arr*Mult + Add
    b = np.array(arr_reflectance, dtype = np.float32)
    np.save(resultfolder + 'Landsat_'+ info +'_B' + str(n_band), b)
    print("save "+ 'Landsat_'+ info +'_B' + str(n_band))
    
