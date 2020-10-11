from Main import Main


def Loading_processing(filepath, X_arr, FIRMS, nameFile, path_res):

    file = open(filepath + r"/result/" + nameFile + '.txt','w')
    file.write('Snapshot, Fire algorithm output pixels, Points coincided with firms, unsure, medium confident, confident')
    
    for i in range(len(X_arr)):
        
        mtl = filepath + '\LC08_L1TP_'+X_arr[i]+'_01_T1\LC08_L1TP_'+X_arr[i]+ '_01_T1_MTL.txt'
        print('MTL',mtl)
        
        main = Main(X_arr[i], filepath, FIRMS, mtl, path_res)
        k_alg      = main[0]# Fire algorithm output pixels
        firms      = main[1]# match with firms
        k_unsure   = main[2]
        k_med_conf = main[3]
        k_conf     = main[4]
        
        fileStr = 'LC08_L1TP_'+X_arr[i]+'_01_T1, ' + str(k_alg)+', '+str(firms)+', '+str(k_unsure)+', '+str(k_med_conf)+', '+str(k_conf)
        
        file.write('\n' + fileStr + '\n')
        
    file.close()    
        
X_arr = ['144015_20190703_20190718', '144015_20190719_20190731', '144015_20190804_20190820', '144015_20190820_20190902']
# '134018_20140528_20170422' '134018_20140715_20170421', '134018_20140731_20170420', '134018_20140816_20170420'

FIRMS = r'\fire_archive_M6_120507.csv'
nameFile = 'Snapshot'
filepath = r'F:\Gis\Snapshots'
path_res = r'F:\Gis\Snapshots\result'
Loading_processing(filepath, X_arr, FIRMS, nameFile, path_res)
    
