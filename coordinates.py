import numpy as np
import matplotlib.pyplot as plt
import tifffile

X = '172022_20180922_20180928'
folder = r'F:\Gis\LC08_L1TP_'+X+'_01_T1'
folder2 = r'\Image\LC08_L1TP_'+X+'_01_T1_MTL.txt'

result = np.load(folder + r'\fire_mask\fire_mask_'+X+'.npy')
b_1s = np.load(folder + r'\numpy\Landsat_'+X+'_B1.npy')

data={}
with open(folder2) as file:
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

def index_corners(b):
    shape = b.shape
    mask = np.zeros(shape)
    
    np.putmask(mask,b!=b[0][0],1)
    
    ind_lines = []
    for i in range(shape[0]):
       if np.sum(mask[i,:])<=5 and np.sum(mask[i,:])!=0:
           ind_lines.append(i)
    
    ind_columns = []   
    for j in range(shape[1]):
       if np.sum(mask[:,j])<=5 and np.sum(mask[:,j])!=0:
           ind_columns.append(j)
           
    Max_ind_line = max(ind_lines)  
    Min_ind_line = min(ind_lines) 
    Max_ind_col = max(ind_columns)
    Min_ind_col = min(ind_columns)
    
    return  (Max_ind_line, Min_ind_line, Max_ind_col, Min_ind_col)
    
def Coordinates(i, j, UL_LAT, LR_LAT, UR_LON, LL_LON, Max_ind_line, Min_ind_line, Max_ind_col, Min_ind_col):
  
    
    offsetX = Min_ind_col 
    offsetY = Min_ind_line
    
    
    Max_Lat = max(UL_LAT,UR_LAT,LL_LAT,LR_LAT)
    
    Min_lat = min(UL_LAT,UR_LAT,LL_LAT,LR_LAT)
    
    Max_lon = max(UL_LON,UR_LON,LL_LON,LR_LON)
    
    Min_lon = min(UL_LON,UR_LON,LL_LON,LR_LON)
    
    p_lat = abs((Max_Lat - Min_lat)/(Max_ind_line - offsetY))
    print(p_lat)
    p_lon = abs((Max_lon - Min_lon)/(Max_ind_col - offsetX))
    print(p_lon)
    
    res_lat1 = Max_Lat - (i - offsetY) * p_lat

    res_lon = Min_lon + (j - offsetX) * p_lon
    
    return (res_lat1,res_lon)


shape = result.shape

height = shape[0]
width = shape[1]

lonarr = []
latarr = []

Corners = index_corners(b_1s)
Max_ind_line = Corners[0]
Min_ind_line = Corners[1]
Max_ind_col = Corners[2]
Min_ind_col = Corners[3]


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






            