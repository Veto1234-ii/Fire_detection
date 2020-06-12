import gc
import numpy as np
import matplotlib.pyplot as plt

X = '176022_20181020_20181031'

folder = r'F:\Gis\LC08_L1TP_'+X+'_01_T1'
b_1s=np.load(folder + r'\numpy\Landsat32_'+X+'_B1.npy')

folder2 = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X+'_01_T1_MTL.txt'
data={}

with open(folder2) as file:
    for line in file:
        key, *value = line.split()
        data[key] = value
 
Add = float(data['REFLECTANCE_ADD_BAND_1'][1])       

shape = b_1s.shape
res1 = np.zeros(shape)
np.putmask(res1, b_1s!=Add , 1)
res2 = np.copy(res1)

for i in range(2,shape[0]-2):
    for j in range(2,shape[1]-2):
        if res1[i][j]==1:
            k = 40
            arr=res1[i-k:i+k,j-k:j+k]
            height = arr.shape[0]
            width = arr.shape[1]
            if np.sum(arr) < height*width :
                res2[i][j]=0
                
res3 = np.array(res2,dtype = bool)        
np.save( 'clip_'+X,res3)
print(np.sum(res2))
