from comparison import *

X_GT = '188034_20140215_20170425'
X_test = '188034_20131229_20170427'
k = 2 # нужное кол-во точек

# 188034_20140623_20170421
# 188034_20140522_20180527
# 188034_20140215_20170425
# 188034_20140319_20170425
# 188034_20131229_20170427
filepath = r'F:\Gis\188034\LC08_L1TP_'+X_GT+'_01_T1\Image\LC08_L1TP_'+X_GT
np_filepath = r'result/'

snapshot1 = X_GT[7:15]
snapshot2 = X_test[7:15]

arr1 = Lists_coordinates(np_filepath, snapshot1)
# Visualization_nparray_coordinates(np_filepath,snapshot1, 'red')
print(len(arr1), 'Points '+snapshot1)

arr2 = Lists_coordinates(np_filepath, snapshot2)
# Visualization_nparray_coordinates(np_filepath, snapshot2, 'blue')
print(len(arr2), 'Points '+snapshot2)

# E = E_coordinates(filepath, np_filepath, X_GT)
# E_lat = E[0]
# E_lon = E[1]

# res1 = compare_coordinates_lists_1(arr1, arr2)
E_diff = Minimum_distance(arr1, arr2, k)
print(E_diff)
res = compare_coordinates_lists(arr1, arr2, E_diff)
print(res)
print(len(res))

# Visualization_arr(res, snapshot1+'_'+snapshot2, 'green')
# file.close()