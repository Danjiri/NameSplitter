import numpy as np
import pandas as pd
import csv

def l_point(appl_data,fullname):
    
    calc_L =[]
    a0 = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []


        #LengthPointの計算
    for i in range(len(fullname)): 
        if len(fullname) == 3:
            if i == 0:
                for j in range(2):
                    calc_L.append(appl_data[i][7 + j] / (appl_data[i][7] + appl_data[i][8]))
            elif i == 1:
                for j in range(2):
                    calc_L.append(appl_data[i][12 - j * 4] / (appl_data[i][8] + appl_data[i][12]))
            elif i == 2:
                for j in range(2):
                    calc_L.append(appl_data[i][12 - j * 1] / (appl_data[i][11] + appl_data[i][12]))
        elif len(fullname) == 4:
            if i == 0:
                for j in range(7,10):
                    calc_L.append(appl_data[i][j] / (appl_data[i][7] + appl_data[i][8] + appl_data[i][9]))
            if i == 1:
                calc_L.append(appl_data[i][13] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][13]))
                calc_L.append(appl_data[i][8] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][13]))
                calc_L.append(appl_data[i][9] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][13]))
            if i == 2:
                calc_L.append(appl_data[i][13] / (appl_data[i][9] + appl_data[i][12] + appl_data[i][13])) 
                calc_L.append(appl_data[i][12] / (appl_data[i][9] + appl_data[i][12] + appl_data[i][13])) 
                calc_L.append(appl_data[i][9] / (appl_data[i][9] + appl_data[i][12] + appl_data[i][13]))           
            if i == 3:
                for j in reversed(range(11,14)):
                    calc_L.append(appl_data[i][j] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13]))
        elif len(fullname) == 5:
            if i == 0:
                for j in range(7,11):
                    calc_L.append(appl_data[i][j] / (appl_data[i][7] + appl_data[i][8] + appl_data[i][9] + appl_data[i][10]))
            if i == 1:
                calc_L.append(appl_data[i][14] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))
                calc_L.append(appl_data[i][8] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))
                calc_L.append(appl_data[i][9] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))
                calc_L.append(appl_data[i][10] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))
            if i == 2:
                calc_L.append(appl_data[i][14] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))
                calc_L.append(appl_data[i][13] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))
                calc_L.append(appl_data[i][9] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))
                calc_L.append(appl_data[i][10] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))
            if i == 3:
                calc_L.append(appl_data[i][14] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                calc_L.append(appl_data[i][13] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                calc_L.append(appl_data[i][12] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                calc_L.append(appl_data[i][10] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))                
            if i == 4:
                for j in reversed(range(11,15)):
                    calc_L.append(appl_data[i][14] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14])) #郎

        elif len(fullname) == 6:
            if i == 0:
                calc_L.append(appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))     #武
                calc_L.append(appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))     #武
                calc_L.append(appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))     #武
                calc_L.append(appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))    #武
                calc_L.append(appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))    #武
            if i == 1:
                calc_L.append(appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))    #者
                calc_L.append(appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))   #者
                calc_L.append(appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))    #者
                calc_L.append(appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))    #者
                calc_L.append(appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))   #者
            if i == 2:
                calc_L.append(appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #小
                calc_L.append(appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #小
                calc_L.append(appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))     #小
                calc_L.append(appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #小
                calc_L.append(appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #小
            if i == 3:
                calc_L.append(appl_data[3][14] / (appl_data[3][10] + appl_data[3][10] + appl_data[3][13] + appl_data[3][14]))   #路
                calc_L.append(appl_data[3][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #路
                calc_L.append(appl_data[3][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #路
                calc_L.append(appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #路
                calc_L.append(appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14]))    #路
            if i == 4:
                calc_L.append(appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14]))    #実
                calc_L.append(appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14]))    #実
                calc_L.append(appl_data[4][13] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14]))    #実
                calc_L.append(appl_data[4][12] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14]))    #実
                calc_L.append(appl_data[4][10] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14]))    #実
            if i == 5:
                calc_L.append(appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14]))    #篤
                calc_L.append(appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14]))    #篤
                calc_L.append(appl_data[5][13] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14]))    #篤
                calc_L.append(appl_data[5][12] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14]))    #篤
                calc_L.append(appl_data[5][11] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14]))    #篤
        elif len(fullname) == 7:
            if i == 0:
                calc_L.append(appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))      #木
                calc_L.append(appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))      #木
                calc_L.append(appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))      #木
                calc_L.append(appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))     #木
                calc_L.append(appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))     #木
                calc_L.append(appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]))     #木
            if i == 1:
                calc_L.append(appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))     #戸
                calc_L.append(appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))      #戸
                calc_L.append(appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))      #戸
                calc_L.append(appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))     #戸
                calc_L.append(appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))    #戸
                calc_L.append(appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14]))    #戸
            if i == 2:
                calc_L.append(appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14]))     #孝
                calc_L.append(appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14]))     #孝
                calc_L.append(appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14]))      #孝
                calc_L.append(appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14]))     #孝
                calc_L.append(appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14]))     #孝
                calc_L.append(appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14]))     #孝
            if i == 3:
                calc_L.append(appl_data[3][14] / (appl_data[3][10] + appl_data[3][14]))     #允
                calc_L.append(appl_data[3][14] / (appl_data[3][10] + appl_data[3][14]))     #允
                calc_L.append(appl_data[3][14] / (appl_data[3][10] + appl_data[3][14]))     #允
                calc_L.append(appl_data[3][10] / (appl_data[3][10] + appl_data[3][14]))     #允
                calc_L.append(appl_data[3][10] / (appl_data[3][10] + appl_data[3][14]))     #允
                calc_L.append(appl_data[3][10] / (appl_data[3][10] + appl_data[3][14]))     #允                
            if i == 4:
                calc_L.append(appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14]))     #犬
                calc_L.append(appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14]))     #犬
                calc_L.append(appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14]))     #犬
                calc_L.append(appl_data[4][13] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14]))     #犬
                calc_L.append(appl_data[4][10] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14]))     #犬
                calc_L.append(appl_data[4][10] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14]))     #犬                
            if i == 5:
                calc_L.append(appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14]))     #養
                calc_L.append(appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14]))     #養
                calc_L.append(appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14]))     #養
                calc_L.append(appl_data[5][13] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14]))     #養
                calc_L.append(appl_data[5][12] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14]))     #養
                calc_L.append(appl_data[5][10] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14]))     #養
            if i == 6:
                calc_L.append(appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14]))     #毅
                calc_L.append(appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14]))     #毅
                calc_L.append(appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14]))     #毅
                calc_L.append(appl_data[6][13] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14]))     #毅
                calc_L.append(appl_data[6][12] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14]))     #毅
                calc_L.append(appl_data[6][11] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14]))     #毅                        
                                ####    5文字以上だけが問題   #####
        else:#8文字以上の名前
            if i == 0:  #1文字目
                for j in range(7,11):
                    a0.append(appl_data[i][j] / (appl_data[i][7] + appl_data[i][8] + appl_data[i][9] + appl_data[i][10]))
                    if j == 10 and len(fullname) > 5:
                        for k in range(len(fullname) - 5):
                            print("k:",k)
                            a0.append(appl_data[i][j] / (appl_data[i][7] + appl_data[i][8] + appl_data[i][9] + appl_data[i][10]))   #ok
            if i == 1:  #2文字目
                a1.append(appl_data[i][14] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))  
                a1.append(appl_data[i][8] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))   
                a1.append(appl_data[i][9] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))    
                a1.append(appl_data[i][10] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14])) #ok
                if len(fullname) > 5:
                    for j in range(len(fullname) - 5):
                        a1.append(appl_data[i][10] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14]))
            if i == 2:  #3文字目    
                a2.append(appl_data[i][14] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))
                a2.append(appl_data[i][14] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))  
                a2.append(appl_data[i][9] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))   
                a2.append(appl_data[i][10] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))    #ok
                if len(fullname) > 5:
                    for j in range(len(fullname) - 5):
                        a2.append(appl_data[i][10] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14]))             
            if i == 3:  #4文字目
                a3.append(appl_data[i][14] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                if len(fullname) > 6:
                    for j in range(len(fullname) - 4):
                        a3.append(appl_data[i][14] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))          
                a3.append(appl_data[i][10] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))   #ok
                if len(fullname) > 5:
                    for j in range(len(fullname) - 5):
                        a3.append(appl_data[i][10] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14])) 
            if i > 3:   #5文字目以上
                a4.append(appl_data[i][14] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                if len(fullname) > 5:   #名前6文字以上
                    for l in range(len(fullname) - 5):
                        print("14のとこ:",i)
                        a4.append(appl_data[i][14] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                a4.append(appl_data[i][13] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                a4.append(appl_data[i][12] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))                      
                if i != len(fullname) -1 and len(fullname) > 5: #5文字以上の名前から、len-1 >  の場合に10が必要   #前から4番目～(最後-1)まで
                    for k in range(len(fullname) - (i + 1)):
#                        print("10のi",i)
#                        print("10のところ",k)
                        a4.append(appl_data[i][10] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
                else: ##一番最後の文字のとき一回だけ通す         #5文字の時 i == 4 #6文字のとき i == 5
#                    print("最後のi") 
#                    print(i)
                    a4.append(appl_data[i][11] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]))
        





    each_lPoint = np.reshape(calc_L, (len(fullname),len(fullname)-1))
#    print(each_lPoint)
    each_lPoint = np.sum(each_lPoint, axis=0)
    each_lPoint = each_lPoint / (len(fullname))
#    print(each_lPoint)

    return each_lPoint



