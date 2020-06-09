import numpy as np


X = '176022_20181020_20181031'

folder = r'F:\Gis\LC08_L1TP_'+X+'_01_T1'

b_1s=np.load(folder + r'\numpy\Landsat32_'+X+'_B1.npy')
shape = b_1s.shape
res1 = np.zeros(shape)
np.putmask(res1, b_1s!=0 , 1)
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
