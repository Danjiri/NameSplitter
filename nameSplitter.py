import numpy as np
import pandas as pd
import csv


def main(fullname):
#    name_length = len(fullname)

    kanji_data = pd.read_csv("kanji.csv", header=None) #CSVファイル読み込み
    
    #numpyの行列作成
    kanji_array = np.array
    kanji_array = kanji_data.values

    appl_data = []

    #入力された漢字データの検索
    for i in range(len(fullname)):
        for l in kanji_array:
            if fullname[i] in l:
                appl_data.append(l)   #該当データ抽出
                

    for i in range(1,len(fullname)):

        #考えられる名前分割パターンの全通り
        tmp_lastname = fullname[0:i]
        tmp_firstname = fullname[i:]
        space = " "
        tmp_name = tmp_lastname + space + tmp_firstname
        print(tmp_name)

    calc = []


    #OrderPointの計算  

    for i in range(1,len(fullname)-1): #後ろから二番目の文字まで計算

        if i == 1 and len(fullname) == 3:    #文字列3文字の場合
            for o in range(3,5):
                    calc.append(appl_data[1][o] / (appl_data[1][3] + appl_data[1][4]))
        elif i == 1 and len(fullname) > 3: #4文字以上の文字列の2文字目の各パターンの確率                     
            for j in reversed(range(2,5)):#1の全パターン                                
                calc.append(appl_data[i][j] / (appl_data[i][2] + appl_data[i][3] + appl_data[i][4]))
                if j == 2 and len(fullname) > 4: #残りの字数分の計算結果の追加 / 姓名が4文字以上の場合
                    for m in range(len(fullname)-4): 
                        calc.append(appl_data[i][j] / (appl_data[i][2] + appl_data[i][3] + appl_data[i][4]))
        else:    #3文字目以降の各パターンの確率
            for k in reversed(range(2,5)):                
                
                if k == 4 and len(fullname) > 3: #名前4文字以上の場合
                    for l in range(i-1):               
                        calc.append(appl_data[i][5] / (appl_data[i][2] + appl_data[i][3] + appl_data[i][4] + appl_data[i][5]))
                if k >= 3:
                    calc.append(appl_data[i][k] / (appl_data[i][2]  + appl_data[i][3] + appl_data[i][4] + appl_data[i][5]))

                if k == 2 and i < len(fullname) - 2 and len(fullname) > 4:
                    for n in range(len(fullname) - (i + 2)):
                        calc.append(appl_data[i][k] / (appl_data[i][2]  + appl_data[i][3] + appl_data[i][4] + appl_data[i][5]))


    each_oPoint = np.reshape(calc, (len(fullname)-2,len(fullname)-1))
    print(each_oPoint)
    each_oPoint = each_oPoint / (len(fullname)-2)
    print("OP:",np.sum(each_oPoint, axis=0))


    a = []
    b = []
    c = []

        #LengthPointの計算
    for i in range(len(fullname)): 
        if len(fullname) == 3:
            if i == 0:
                for j in range(3):
                    a.append(appl_data[i][7 + j] / (appl_data[i][7] + appl_data[i][8]))
            elif i == 1:
                for j in range(3):
                    b.append(appl_data[i][12 - j * 4] / (appl_data[i][8] + appl_data[i][12]))
            elif i == 2:
                for j in range(3):
                    c.append(appl_data[i][12 - j * 1] / (appl_data[i][11] + appl_data[i][12]))  #3文字の名前ok
        elif len(fullname) == 4:
            if i == 0:
                for j in range(7,10):
                    appl_data[i][j] / (appl_data[i][7] + appl_data[i][8] + appl_data[i][9])
            if i == 1:
                appl_data[i][13] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][13])
                appl_data[i][8] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][13])
                appl_data[i][9] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][13])
            if i == 2:
                appl_data[i][13] / (appl_data[i][9] + appl_data[i][12] + appl_data[i][13]) 
                appl_data[i][12] / (appl_data[i][9] + appl_data[i][12] + appl_data[i][13]) 
                appl_data[i][9] / (appl_data[i][9] + appl_data[i][12] + appl_data[i][13])              
            if i == 3:
                for j in reversed(range(11,14)):
                    appl_data[i][j] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13]) 
        else:#5文字以上
            if i == 0:
                for j in range(7,11):
                    appl_data[i][j] / (appl_data[i][7] + appl_data[i][8] + appl_data[i][9] + appl_data[i][10])
                    if j == 10 and len(fullname) > 5:
                        for k in range(len(fullname) - 5):
                            appl_data[i][j] / (appl_data[i][7] + appl_data[i][8] + appl_data[i][9] + appl_data[i][10])
            if i == 1:
                appl_data[i][14] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14])  
                appl_data[i][8] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14])   
                appl_data[i][9] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14])    
                appl_data[i][10] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14])
                if len(fullname) > 5:
                    for j in range(len(fullname) - 5):
                        appl_data[i][10] / (appl_data[i][8] + appl_data[i][9] + appl_data[i][10] + appl_data[i][14])
            if i == 2:
                appl_data[i][14] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14])  
                appl_data[i][13] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14])  
                appl_data[i][9] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14])   
                appl_data[i][10] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14])
                if len(fullname) > 5:
                    for j in range(len(fullname) - 5):
                        appl_data[i][10] / (appl_data[i][9] + appl_data[i][10] + appl_data[i][13] + appl_data[i][14])             
            if i == 3:
                appl_data[i][14] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史1
                appl_data[i][13] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史1
                appl_data[i][12] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史1
                appl_data[i][10] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史1
                if len(fullname) > 5:
                    for j in range(len(fullname) - 5):
                        appl_data[i][10] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) 
            if i == 4:
                for j in reversed(range(11,15)):
                    appl_data[i][14] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史2
                    appl_data[i][13] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史2
                    appl_data[i][12] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史2
                    appl_data[i][11] / (appl_data[i][11] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14]) #史2                       
                if len(fullname) > 5 and j == 11:
                    for k in range(len(fullname) - 5):
                        appl_data[i][j] / (appl_data[i][10] + appl_data[i][12] + appl_data[i][13] + appl_data[i][14])                     

    print(a)
    print(b)
    print(c)

"""
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])  #坂
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])  #坂
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]) #坂
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]) #坂


        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])  #本
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])   #本
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])    #本
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #本
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #者


        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])  #敦
        appl_data[2][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])  #敦
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])   #敦
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])  #敦
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])  #小

        appl_data[3][14] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[3][13] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[3][12] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[3][10] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
         appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路

        appl_data[4][14] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2
        appl_data[4][13] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2
        appl_data[4][12] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2
        appl_data[4][11] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2
"""



"""     #LengthPointの計算 ## 3文字の場合

        #1
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8])    #平

        appl_data[1][12] / (appl_data[1][8] + appl_data[1][12])       #井
        appl_data[2][12] / (appl_data[2][11] + appl_data[2][12])      #堅

        #2
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8])    #平
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][12])       #井

        appl_data[2][11] / (appl_data[2][11] + appl_data[2][12])      #堅

============================================================================================================

        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8])    #平        
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8])    #平

        appl_data[1][12] / (appl_data[1][8] + appl_data[1][12])       #井
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][12])       #井

        appl_data[2][12] / (appl_data[2][11] + appl_data[2][12])      #堅
        appl_data[2][11] / (appl_data[2][11] + appl_data[2][12])      #堅

"""

"""
        #LengthPointの計算 ## 4文字の場合
        #1
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9])    #坂

        appl_data[1][13] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])       #本
        appl_data[2][13] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])      #敦
        appl_data[3][13] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13])     #史
        #2
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9])  #坂
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])   #本

        appl_data[2][12] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])  #敦
        appl_data[3][12] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13]) #史    
        #3
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9]) #坂
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])    #本
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])   #敦

        appl_data[3][11] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13]) #史

============================================================================================================
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9])  #坂
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9])  #坂
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9])  #坂

        appl_data[1][13] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])  #本
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])   #本
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])   #本

        appl_data[2][13] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])  #敦
        appl_data[2][12] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])  #敦
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])   #敦

        appl_data[3][13] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13]) #史
        appl_data[3][12] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13]) #史
        appl_data[3][11] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13]) #史

"""

"""
        #LengthPointの計算 ## 5文字の場合
        #1
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #坂

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])       #本
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])      #敦
        appl_data[3][14] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14])     #史1
        appl_data[4][14] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14])     #史2

        #2
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])  #坂
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])   #本

        appl_data[2][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])  #敦
        appl_data[3][13] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[4][13] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14])     #史2    

        #3
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]) #坂
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])    #本
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])   #敦

        appl_data[3][12] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[4][12] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14])     #史2

        #4
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]) #坂
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #本
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])   #敦
        appl_data[3][10] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1

        appl_data[4][11] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14])     #史2

============================================================================================================
        #5文字
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])  #坂
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])  #坂
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]) #坂
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10]) #坂

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])  #本
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])   #本
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])    #本
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #本

        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])  #敦
        appl_data[2][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])  #敦
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])   #敦
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])  #敦

        appl_data[3][14] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[3][13] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[3][12] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1
        appl_data[3][10] / (appl_data[2][10] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史1

        appl_data[4][14] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2
        appl_data[4][13] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2
        appl_data[4][12] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2
        appl_data[4][11] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13] + appl_data[2][14]) #史2


"""

""" 
    LengthPointの計算   ## 6文字の場合 ##
        #1
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #武

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][10])    #者
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][10] + appl_data[3][13] + appl_data[3][14])    #路
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤

        #2
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #武
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][10])    #者

        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小
        appl_data[3][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤

        #3
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #武
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][10])    #者
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小

        appl_data[3][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[4][13] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[5][13] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤      

        #4
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #武
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][10])    #者
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])     #小
        appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路

        appl_data[4][12] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[5][12] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤

        #5
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #武
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])    #者
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小
        appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実

        appl_data[5][11] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤    

============================================================================================================
        6文字
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #武
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #武
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #武
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #武
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])    #武

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])    #者
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #者
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #者
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])    #者
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])    #者

        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小     
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])     #小
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小

        appl_data[3][14] / (appl_data[3][10] + appl_data[3][10] + appl_data[3][13] + appl_data[3][14])   #路
        appl_data[3][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[3][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路

        appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][13] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][12] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実

        appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][13] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][12] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][11] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤

============================================================================================================                  

"""

"""     #orderpoint
        #5文字の場合
        appl_data[2][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5])   #敦 3
        appl_data[2][4] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3
        appl_data[2][3] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3
        appl_data[2][2] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3

###
        ##1周目
        appl_data[1][4] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4])   #本 2
        appl_data[2][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5])   #敦 3
        appl_data[3][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5])
        ##2周目
        appl_data[1][3] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4])  #本 2
        appl_data[2][4] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3
        appl_data[3][5]
        ##3周目
        appl_data[1][2] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4]) #本 2
        appl_data[2][3] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3
        appl_data[3][4] / (appl_data[3][2] + appl_data[3][3] + appl_data[3][4] + appl_data[2][5])
        ##順番
        appl_data[1][4] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4])   #本 2
        appl_data[1][3] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4])  #本 2
        appl_data[1][2] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4]) #本 2
        appl_data[2][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5])   #敦 3
        appl_data[2][4] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3
        appl_data[2][3] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3
        appl_data[i][5 - (1~3, 0~3)] /(appl_data[i][2] + appl_data[i][3] + appl_data[i][4] + appl_data[i][5])
        appl_data[i][5 - (1~3, 0~3)] /(appl_data[i][2] + appl_data[i][3] + appl_data[i][4] + appl_data[i][5])
###        
"""
"""
    ##1周目

        appl_data[1][4] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4]) 者
        appl_data[2][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 小  
        appl_data[3][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 路   
        appl_data[4][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 実 

    ##2周目

        appl_data[1][3] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4]) 者
        appl_data[2][4] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 小  
        appl_data[3][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 路   
        appl_data[4][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 実

    ##3周目

        appl_data[1][2] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4]) 者
        appl_data[2][3] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 小  
        appl_data[3][4] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 路   
        appl_data[4][5] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 実 

    ##4周目
        appl_data[1][2] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4]) 者
        appl_data[2][2] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 小  
        appl_data[3][3] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 路   
        appl_data[4][4] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 実 


    ##5周目

        appl_data[1][2] / (appl_data[1][2] + appl_data[1][3] + appl_data[1][4]) 者
        appl_data[2][2] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 小  
        appl_data[3][2] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 路   
        appl_data[4][3] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) 実 


"""







"""
    for i in range(len(fullname)):
        for l in range(1,14):
            order_point = appl_data[i][l]
            length_point = 
    surname
    name  [][]+[][] /(len(fullname) - 1)
"""        


print("==== Enter 'exit' to stop this app. ====")

while True:
    
    name = input('Enter your name:')        

    blank1 = ' ' in name
    blank2 = '　' in name
    
    if name == 'exit':
        break  

    if blank1 == True or blank2 == True:
        print('---- It\'s written properly. ----')

    if len(name) == 2:
       last = name[0:1]
       first = name[1:]
       space = " "
       print(last + space + first)
    else:
        main(name)    
        print('---- next ----')
