import numpy as np
import math
import datetime
from comparison import compare_coordinates_lists
from comparison import To_radians
from comparison import Lists_coordinates


np_folder = r'result/'


def Print_Dict(d):
    for key,value in d.items():
        # print(key,value[2],' days')
        print(key,value[1],' points')
        
def time(a, b):
    date1 = datetime.date(int(a[0:4]),int(a[4:6]),int(a[6:]))
    date2 = datetime.date(int(b[0:4]),int(b[4:6]),int(b[6:]))
    days = abs(int(str(date1-date2).split()[0]))
    return days

def Analysis(np_folder, Names_images, E_diff): 
    
    d2 ={}
    for i in range(len(Names_images)-1):
        arr1 = Lists_coordinates(np_folder, Names_images[i])
        
        for j in range(i+1, len(Names_images)):
            
            arr2 = Lists_coordinates(np_folder, Names_images[j])
            res = compare_coordinates_lists(arr1, arr2, E_diff)
            Time = time(Names_images[i], Names_images[j])
            if len(res)!=0:
                d2[(Names_images[i],Names_images[j])] = (res, len(res), Time)
    return d2

def comparison_comparison(d2, Names_images):
    d3 = {}
    for key, value in d2.items():
        for i in range(len(Names_images)):
            if Names_images[i] in key:
                continue
            else:
                arr2 = Lists_coordinates(np_folder, Names_images[i])
                res = compare_coordinates_lists(value[0], arr2)
                if len(res)!=0:
                    d3[key + (Names_images[i],)] = (res, len(res))
    return d3    

Names_images = ['20140623', '20140522', '20140319', '20140215', '20131229']
E_diff = 0.009164408392108444# minimum distane 20140623 and 20131229
d2 = Analysis(np_folder, Names_images, E_diff)
Print_Dict(d2)
print()
print()
  
# d3 = comparison_comparison(d2, Names_images)
# Print_Dict(d3)
# print()
# print()

# d4 = comparison_comparison(d3, Names_images)
# Print_Dict(d4)
# print()
# print()


# time  = time('20140623', '20140522')
# print(time)


