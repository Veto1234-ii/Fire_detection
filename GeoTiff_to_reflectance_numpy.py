
import numpy as np
import tifffile
X = '174022_20191009_20191018'

folder = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X+'_01_T1_B'
folder2 = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X+'_01_T1_MTL.txt'
data={}

with open(folder2) as file:
    for line in file:
        key, *value = line.split()
        data[key] = value
         
for  i in range(7):
    image = tifffile.imread(folder + str(i+1)+'.tif', key=0)
    arr = np.array(image)
    Mult = float(data['REFLECTANCE_MULT_BAND_'+str(i+1)][1])
    Add = float(data['REFLECTANCE_ADD_BAND_'+str(i+1)][1])
    arr_reflectance = arr*Mult + Add
    b = np.array(arr_reflectance,dtype = np.float32)
    np.save('Landsat_'+ X +'_B' + str(i+1), b)
