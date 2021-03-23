import rasterio
import pyproj
import numpy as np




folder = r'D:\MODIS\script\result\Article_coordinates'

info = ['188034_20140623_20170421', 
        '026048_20140507_20170306', '105069_20140805_20170420',
        '226069_20140820_20170420', '227069_20140624_20170421']



def Coordinates_gdal(folder, info):
    
    localname = folder+ '/LC08_L1TP_'+info+'_01_T1_B6.TIF'
    folder_firemask = r'D:\MODIS\script\result\Article_coordinates\fire_mask_'+info+'.npy'
    
    firemask = np.load(folder_firemask)

    with rasterio.open(localname, mode='r') as src:
        p = pyproj.Proj(src.crs)
        
        height = src.height
        width  = src.width
        
        lonarr = []
        latarr = []
        
        for i in range(height):
            for j in range(width):
                
                if (i == height//2) and (j == width//2):
                    x_center, y_center = src.xy(i, j)
                    lon_center, lat_center = p(x_center, y_center, inverse=True) 
                    
                if firemask[i][j]!=0:
                    x, y = src.xy(i, j)
                    lon, lat = p(x,y,inverse=True) 
                    
                    latarr.append(lat)
                    lonarr.append(lon)
                        
                
                    
        
        lonarr=np.array(lonarr)
        latarr=np.array(latarr)
        
        np.save(folder+'\latarr_gdal_'+info, latarr)
        np.save(folder+'\lonarr_gdal_'+info, lonarr)         
        print('coords done')
        
for x in info:
    Coordinates_gdal(folder, x)