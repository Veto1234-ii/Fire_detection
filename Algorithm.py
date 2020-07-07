# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:33:14 2020

@author: Катя
"""
import gc
import numpy as np
import matplotlib.pyplot as plt
from Layer import Layer

def detectFire(np_folder, info):

    b_1s=np.load(np_folder + r'Landsat_'+info+'_B1.npy')
    b_2s=np.load(np_folder + r'Landsat_'+info+'_B2.npy')
    b_3s=np.load(np_folder + r'Landsat_'+info+'_B3.npy')
    b_4s=np.load(np_folder + r'Landsat_'+info+'_B4.npy')
    b_5s=np.load(np_folder + r'Landsat_'+info+'_B5.npy')
    b_6s=np.load(np_folder + r'Landsat_'+info+'_B6.npy')
    b_7s=np.load(np_folder + r'Landsat_'+info+'_B7.npy')

    shape=b_1s.shape
    data = np.full(shape, True, dtype=bool)

    l1 = Layer(b_1s)
    l2 = Layer(b_2s)
    l3 = Layer(b_3s)
    l4 = Layer(b_4s)
    l5 = Layer(b_5s)
    l6 = Layer(b_6s)
    l7 = Layer(b_7s)
    ldata = Layer(data)

    nw2 = ldata & ((l3 > l2) | (l1 > l2) & (l2 > l3) &  (l3 > l4) )

    l3.arr = None
    l3 = None
    gc.collect()

    l2.arr = None
    l2 = None
    gc.collect()

    Sub_1_7 = l1 - l7
    nw1 = ldata &  (l4 > l5) & (l5 > l6) &  (l6 > l7) & (Sub_1_7 < 0.2)

    l4.arr = None
    l4 = None
    gc.collect()

    Sub_1_7.arr = None
    Sub_1_7 = None
    gc.collect()

    z1 = nw1 & nw2
    not_water = ~z1

    # z1.arr = None
    # z1 = None
    # gc.collect()

    result=np.zeros(shape,dtype = np.uint8)

    Div_7_6 = l7/l6
    Div_7_5 = l7/l5

    Sub_7_5 = l7 - l5

    np.putmask(result, (ldata &  (Sub_7_5 > 0.17) & (Div_7_5 > 1.8)  &  (Div_7_6  > 1.6 ) ).arr , 3 )

    Div_7_6.arr = None
    Div_7_6 = None
    gc.collect()

    # np.putmask(result, np.logical_and( data==1, np.logical_and( np.logical_and(b_7s > 0.5,  Div_7_5 > 2.5), Sub_7_5 > 0.3 ) ), 1 )
    np.putmask(result, (ldata &  (l7 > 0.5) &  (Div_7_5 > 2.5) & (Sub_7_5 > 0.3 )).arr, 1 )

    Div_7_5.arr = None
    Div_7_5 = None
    gc.collect()

    Sub_7_5.arr = None
    Sub_7_5 = None
    gc.collect()
    # ===================================

    # np.putmask(result, np.logical_and(data==1, np.logical_and( np.logical_and(b_6s > 0.8, b_1s < 0.2),np.logical_or(b_5s > 0.4, b_7s < 0.1))), 2)
    np.putmask(result, (ldata & (l6 > 0.8) & (l1 < 0.2) & ( (l5 > 0.4) | (l7 < 0.1 )) ).arr, 2)

    l1.arr = None
    l1 = None
    gc.collect()

    l6.arr = None
    l6 = None
    gc.collect()
    # ====================================

    for i in range(shape[0]):
        for j in range(shape[1]):
            if result[i][j]==3 and data[i][j]:


                b_5_61=b_5s[i-30:i+31,j-30:j+31]
                b_7_61=b_7s[i-30:i+31,j-30:j+31]

                data61 = data[i-30:i+31,j-30:j+31]
                not_water61 = not_water[i-30:i+31,j-30:j+31]
                result61 = result[i-30:i+31,j-30:j+31]

                shape61 = b_5_61.shape
                arr_7 = []
                arr_5 = []

                for x in range(shape61[0]):
                    for y in range(shape61[1]):

                        if b_7_61[x][y]>0 and not_water61[x][y] and data61[x][y] and result61[x][y]==0:
                            arr_7.append(b_7_61[x][y])
                            arr_5.append(b_5_61[x][y])

                arr_7 = np.array(arr_7)
                arr_5 = np.array(arr_5)

                Div_7_5 = arr_7 / arr_5
    #            print(R75)
                Sr_7=np.mean(arr_7)
                Sr_5=np.mean(arr_5)

                Div_Sr7_Sr5=Sr_7/Sr_5
                Stand7=np.std(arr_7)

                Stand75=np.std(Div_7_5)
                if l7[i][j] > Sr_7 + max(3*Stand7,0.08):
                    if l7[i][j] / l5[i][j] > Div_Sr7_Sr5 + max(3*Stand75,0.8):
                        result[i][j]=3
    #===============================================================================
    plt.title("result")
    plt.imshow(result,cmap='gray')
    np.save(np_folder + 'fire_mask_'+info,result)
    print(np.max(result))
    print(np.sum(result))
    mask = np.zeros(shape, dtype = np.uint8)
    np.putmask(mask,result!=0, 1)
    print(np.sum(mask),'Points ')
