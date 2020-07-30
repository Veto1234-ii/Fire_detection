import matplotlib.pyplot as plt
import numpy as np
from utilities import getMTL

def Visualization_nparray_coordinates(np_folder,info, color):
    
    latarr = np.load(np_folder + r'latarr_'+info+'.npy')
    lonarr = np.load(np_folder + r'lonarr_'+info+'.npy')
    
    
    
    # file  = open(np_folder + r'coordinates_'+info+'.txt','w')
    # for i in range(len(lonarr)):
    #     file.write( str(latarr[i]) + ', '+ str(lonarr[i]) + '\n')
    # file.close()
    
    y = latarr
    x = lonarr
    
    
    
    fig, ax = plt.subplots()
    
    ax.scatter(x, y,
                c = color) 
      
    
    ax.set_facecolor('white')     #  цвет области Axes
    
    fig.set_figwidth(10)     #  ширина и
    fig.set_figheight(10)    #  высота "Figure"
    
    plt.title(info)
    plt.show()

def Visualization_arr(arr, info, color):
    y = [i[0] for i in arr]
    x = [i[1] for i in arr]
    
    
    
    fig, ax = plt.subplots()
    
    ax.scatter(x, y,
                c = color) 
      
    
    ax.set_facecolor('white')     #  цвет области Axes
    
    fig.set_figwidth(10)     #  ширина и
    fig.set_figheight(10)    #  высота "Figure"
    
    plt.title(info)
    plt.show()

