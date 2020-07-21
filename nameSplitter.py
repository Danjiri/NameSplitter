import numpy as np
import pandas as pd
import csv


def main(fullname):


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

    print(appl_data)
    name_pattern = []
    for i in range(1,len(fullname)):
        #考えられる名前分割パターンの全通り
        tmp_lastname = fullname[0:i]
        tmp_firstname = fullname[i:]
        space = " "
        name_pattern.append(tmp_lastname + space + tmp_firstname)
        
    print(name_pattern)
    calc = []


    #OrderPointの計算  

    for i in range(1,len(fullname)-1): #後ろから二番目の文字まで計算

        if i == 1 and len(fullname) == 3:    #文字列3文字の場合
            for o in reversed(range(3,5)):
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


#    print(calc)
    each_oPoint = np.reshape(calc, (len(fullname)-2,len(fullname)-1))
#    print(each_oPoint)
    each_oPoint = np.sum(each_oPoint, axis=0)
    
    each_oPoint = each_oPoint / (len(fullname)-2)
    print(each_oPoint)


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
                    print(i)
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


#    print(calc_L)

#    print("a0",a0)
#    print("a1",a1)
#    print("a2",a2)
#    print("a3",a3)
#    print("a4",a4)



    each_lPoint = np.reshape(calc_L, (len(fullname),len(fullname)-1))
#    print(each_lPoint)
    each_lPoint = np.sum(each_lPoint, axis=0)
    each_lPoint = each_lPoint / (len(fullname))
    print(each_lPoint)

    #判定
    judge_name = []
    for i in range(0,len(fullname) - 1):
        judge_name.append(each_lPoint[i] + each_oPoint[i])
    
    print(name_pattern[np.argmax(judge_name)])
#    print(judge_name)
   

"""作業中のやつ
        
        ##8文字の時


        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #西
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #西
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西



        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])      #園
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])      #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園



        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])      #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺




        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公



        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望





        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14)      #勝
        appl_data[5][13] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14)      #勝
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝


        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][13] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][12] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][10] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海




        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟        
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][13] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][12] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][11] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟


=========

        #3文字目

        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小     
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])     #小
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #小

        #4文字目

        appl_data[3][14] / (appl_data[3][10] + appl_data[3][10] + appl_data[3][13] + appl_data[3][14])   #路
        appl_data[3][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[3][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路
        appl_data[3][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[0][14])    #路


        #5文字目

        appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][13] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][12] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][12] + appl_data[4][13] + appl_data[3][14])    #実

        #6文字目
        appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][14] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][13] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][12] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
        appl_data[5][11] / (appl_data[5][11] + appl_data[5][12] + appl_data[5][13]+ appl_data[3][14])    #篤
                            10の数
        6| i == 4 (5文字目) -> 1     5文字目 -> 0
        7| i == 4  i+1      -> 2     6文字目 -> 1
        8| i == 4           -> 3     7文字目 -> 2
=
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
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])#石

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次
        appl_data[4][14] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎

        #2
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])#石
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原

        appl_data[2][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕
        appl_data[3][13] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次
        appl_data[4][13] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎

        #3
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][9] + appl_data[0][10] + appl_data[0][14])#石
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕

        appl_data[3][12] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次        
        appl_data[4][12] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎

        #4
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])#石
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次
        
        appl_data[4][11] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎

============================================================================================================

        #5文字
        
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])#石
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])#石
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][9] + appl_data[0][10] + appl_data[0][14])#石
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])#石

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])#原

        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕
        appl_data[2][13] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][13] + appl_data[2][14])#裕

        appl_data[3][14] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次
        appl_data[3][13] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次
        appl_data[3][12] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][12] + appl_data[3][13] + appl_data[3][14])#次

        appl_data[4][14] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎
        appl_data[4][13] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎
        appl_data[4][12] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎
        appl_data[4][11] / (appl_data[4][11] + appl_data[4][12] + appl_data[4][13] + appl_data[4][14])#郎

      
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

"""
    LengthPointの計算   ## 7文字の場合 ##



        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅



        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅



        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝

        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅



        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #允
        
        appl_data[4][13] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[5][13] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[6][13] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅



        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬

        appl_data[5][12] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[6][12] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅



        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養

        appl_data[6][11] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅

============================================================================================================         

        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #木
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #木
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #木
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #木



        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])      #戸
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])      #戸
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #戸



        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])      #孝
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #孝



        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #允
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #允


        appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[4][13] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][13] + appl_data[4][14])     #犬


        appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[5][13] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[5][12] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][12] + appl_data[5][13] + appl_data[5][14])     #養



        appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅
        appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅
        appl_data[6][14] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅                
        appl_data[6][13] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅
        appl_data[6][12] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅
        appl_data[6][11] / (appl_data[6][11] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #毅


"""

"""
    LengthPointの計算   ## 8文字の場合 ##




        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西

        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟





        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園

        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟





        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺

        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟





        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公

        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14)     #勝
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟





        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望

        appl_data[5][13] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14)     #勝
        appl_data[6][13] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[7][13] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟




        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])      #勝

        appl_data[6][12] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[7][12] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟




        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[6][10] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海

        appl_data[7][11] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟



============================================================================================================  

        ##8文字の時


        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #西
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #西
        appl_data[0][9] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])      #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西
        appl_data[0][10] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9] + appl_data[0][10])     #西



        appl_data[1][14] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])      #園
        appl_data[1][9] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])      #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園
        appl_data[1][10] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][10] + appl_data[1][14])     #園



        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][14] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][9] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])      #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺
        appl_data[2][10] / (appl_data[2][9] + appl_data[2][10] + appl_data[2][14])     #寺




        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][14] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公
        appl_data[3][10] / (appl_data[3][10] + appl_data[3][14])     #公



        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][14] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望
        appl_data[4][10] / (appl_data[4][10] + appl_data[4][14])     #望





        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][14] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14)      #勝
        appl_data[5][13] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14)      #勝
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝
        appl_data[5][10] / (appl_data[5][10] + appl_data[5][13] + appl_data[5][14])     #勝


        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][14] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][13] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][12] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海
        appl_data[6][10] / (appl_data[6][10] + appl_data[6][12] + appl_data[6][13] + appl_data[6][14])     #海




        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟        
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][14] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][13] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][12] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟
        appl_data[7][11] / (appl_data[7][11] + appl_data[7][12] + appl_data[7][13] + appl_data[7][14])     #舟


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
