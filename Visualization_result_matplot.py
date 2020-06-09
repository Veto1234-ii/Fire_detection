import matplotlib.pyplot as plt
import numpy as np

X = '176022_20181020_20181031'

latarr = np.load(r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Coordinates\latarr_'+X+'.npy')
lonarr = np.load(r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Coordinates\lonarr_'+X+'.npy')



file  = open(r'F:\Gis\LC08_L1TP_'+X+'_01_T1\Coordinates\coordinates.txt','w')
for i in range(len(lonarr)):
    file.write( str(latarr[i]) + ', '+ str(lonarr[i]) + '\n')
file.close()

y = latarr
x = lonarr



fig, ax = plt.subplots()

ax.scatter(x, y,
            c = 'red') 
  

ax.set_facecolor('white')     #  цвет области Axes

fig.set_figwidth(10)     #  ширина и
fig.set_figheight(10)    #  высота "Figure"


plt.show()


            

