from comparison import *

X_1 = '188034_20131229_20170427'
X_2 = '188034_20140215_20170425'
k = 1 # нужное кол-во точек

# 188034_20140623_20170421
# 188034_20140522_20180527
# 188034_20140215_20170425
# 188034_20140319_20170425
# 188034_20131229_20170427

filepath = r'F:\Gis\188034\LC08_L1TP_'+X_1+'_01_T1\Image\LC08_L1TP_'+X_1
np_filepath = r'result/'

snapshot1 = X_1[7:15]
snapshot2 = X_2[7:15]

arr1 = Lists_coordinates(np_filepath, snapshot1)
arr2 = Lists_coordinates(np_filepath, snapshot2)

arrays = Minimum_Len_array(arr1, arr2)
Test_sample_coord = arrays[0]
GT_coord = arrays[1]

print(len(Test_sample_coord), 'Points Test_sample')
print(len(GT_coord), 'Points Ground truth')

days = time(snapshot1, snapshot2)
print(days, 'days')

# E = E_coordinates(filepath, np_filepath, X_GT)
# E_lat = E[0]
# E_lon = E[1]

# res1 = compare_coordinates_lists_1(arr1, arr2)
func = Minimum_distance(GT_coord, Test_sample_coord, k)
E_diff_d = func[0]
E_diff_m = func[1]
print('min E_diff in degrees', E_diff_d)
print('min E_diff in meters', E_diff_m)

dist_points = Dist_GT_test(GT_coord, Test_sample_coord)
# print(dist_points)
# dist_point_sort = dist_points.sort(key = lambda x: (x[0], x[1]))
dist_point_sort = sorted(dist_points, key = lambda x: x[0])
print()
print(dist_point_sort)
print()
print(GT_coord[59][0], GT_coord[59][1], '60 point in Ground truth')
print()
print(Test_sample_coord[6][0], Test_sample_coord[6][1], '7 point in Test_sample')
print(Test_sample_coord[18][0], Test_sample_coord[18][1], '19 point in Test_sample')
print(Test_sample_coord[24][0], Test_sample_coord[24][1], '25 point in Test_sample')


# res = compare_coordinates_lists(arr1, arr2, E_diff_d)
# print(len(res), 'points')
# print(res)

# Visualization_arr(res, snapshot1+'_'+snapshot2, 'green')
# file.close()