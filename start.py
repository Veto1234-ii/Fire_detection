from Main import Main


def Loading_processing(filepath, X_arr, FIRMS, nameFile):

    file = open(filepath + r"/result/" + nameFile + '.txt','w')
    file.write('Snapshot, Fire algorithm output pixels, Points coincided with firms, unsure, medium confident, confident'+'\n')
    
    for i in range(len(X_arr)):
        
        mtl = filepath + '\LC08_L1TP_'+X_arr[i]+'_01_T1\LC08_L1TP_'+X_arr[i]+ '_01_T1_MTL.txt'
        print('MTL',mtl)
        
        main = Main(X_arr[i], filepath, FIRMS, mtl)
        k_alg      = main[0]# Fire algorithm output pixels
        firms      = main[1]# match with firms
        k_unsure   = main[2]
        k_med_conf = main[3]
        k_conf     = main[4]
        
        fileStr = 'LC08_L1TP_'+X_arr[i]+'_01_T1, ' + str(k_alg)+', '+str(firms)+', '
        fileStr+=str(k_unsure)+', '+str(k_med_conf)+', '+str(k_conf)
        
        file.write(fileStr + '\n')
        
    file.close()    
        
X_arr = ['176022_20181020_20181031']

FIRMS = r'fire_archive_M6_120507.csv'
nameFile = 'Snapshot'
filepath = 'F:\Gis\Snapshots'

Loading_processing(filepath, X_arr, FIRMS, nameFile)
    
