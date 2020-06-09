import numpy as np
import matplotlib.pyplot as plt
import tifffile

X = '176022_20181020_20181031'
folder = r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Image\LC08_L1TP_'+X+'_01_T1_MTL.txt'
result = np.load(r'F:\Gis\LC08_L1TP_176022_20181020_20181031_01_T1\fire_mask\fire_mask_'+X+'.npy')
data={}
with open(folder) as file:
    for line in file:
        key, *value = line.split()
        data[key] = value

UL_LAT = float(data['CORNER_UL_LAT_PRODUCT'][1])
UL_LON = float(data['CORNER_UL_LON_PRODUCT'][1])
UR_LAT = float(data['CORNER_UR_LAT_PRODUCT'][1])
UR_LON = float(data['CORNER_UR_LON_PRODUCT'][1])
LL_LAT = float(data['CORNER_LL_LAT_PRODUCT'][1])
LL_LON = float(data['CORNER_LL_LON_PRODUCT'][1])
LR_LAT = float(data['CORNER_LR_LAT_PRODUCT'][1])
LR_LON = float(data['CORNER_LR_LON_PRODUCT'][1])

def Coordinates(height,width,i,j,UL_LAT,LR_LAT,UR_LON,LL_LON):

    ind_UL = (11,1664)
    ind_LR = (7939, 6180)
    ind_LL = (6304, 21)
    ind_UR = (1609, 7841)
    
    offsetX = ind_LL[1] 
    offsetY = ind_UL[0]
    
    width = ind_LR[1] - offsetX
    height = ind_LR[0] - offsetY
    
    p_lat = abs((UL_LAT - LR_LAT)/(ind_LR[0] - ind_UL[0]))
    p_lon = abs((UR_LON - LL_LON)/(ind_UR[1] - ind_LL[1]))
    # res_lat = LR_LAT + (ind_LR[0] - i) *p_lat
    res_lat1 = UL_LAT - (i - offsetY) * p_lat

    res_lon = LL_LON + (j - offsetY) * p_lon
    
    return (res_lat1,res_lon)

shape = result.shape

height = shape[0]
width = shape[1]

lonarr = []
latarr = []



for i in range(height):
        for j in range(width):
            if result[i][j]!=0:
                lon_lat = Coordinates(height,width,i,j,UL_LAT,LR_LAT,UR_LON,LL_LON)
                latarr.append(lon_lat[0])
                lonarr.append(lon_lat[1])
                
               
lonarr=np.array(lonarr)
latarr=np.array(latarr)  
  
print(len(lonarr))            
np.save('lonarr_'+X,lonarr)   
np.save('latarr_'+X,latarr)    
print('well done')       

# # for i in range(len(latarr)):
# #     file.write(str(latarr[i]) + ', ')
# # file.write('\n')

# # for i in range(len(lonarr)):
# #     file.write(str(lonarr[i]) + ', ')
# # file.write('\n')

# for i in range(len(lonarr)):
#     file.write( str(latarr[i]) + ', '+ str(lonarr[i]) + '\n')

# file.close()
# print('well done')   


# UL_LAT = float(data['CORNER_UL_LAT_PRODUCT'][1])
# UL_LON = float(data['CORNER_UL_LON_PRODUCT'][1])
# UR_LAT = float(data['CORNER_UR_LAT_PRODUCT'][1])
# UR_LON = float(data['CORNER_UR_LON_PRODUCT'][1])
# LL_LAT = float(data['CORNER_LL_LAT_PRODUCT'][1])
# LL_LON = float(data['CORNER_LL_LON_PRODUCT'][1])
# LR_LAT = float(data['CORNER_LR_LAT_PRODUCT'][1])
# LR_LON = float(data['CORNER_LR_LON_PRODUCT'][1])






            