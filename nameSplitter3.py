import numpy as np
import pandas as pd
import csv
import lpoint

def name_patterns(fullname):

    name_patterns = []
    for i in range(1,len(fullname)):
        #考えられる名前分割パターンの全通り
        tmp_lastname = fullname[0:i]
        tmp_firstname = fullname[i:]
        space = " "
        name_patterns.append(tmp_lastname + space + tmp_firstname)
        
    return name_patterns

def kanji_search(fullname):
    
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

    return appl_data

def o_point(appl_data,fullname):
    calc = []

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


    each_oPoint = np.reshape(calc, (len(fullname)-2,len(fullname)-1))
    each_oPoint = np.sum(each_oPoint, axis=0)    
    each_oPoint = each_oPoint / (len(fullname)-2)
 

    return each_oPoint


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

def judge(each_lPoint,each_oPoint,fullname):
    #判定
    judge_name = []
    for i in range(0,len(fullname) - 1):
        judge_name.append(each_lPoint[i] + each_oPoint[i])
    
    return name_pattern[np.argmax(judge_name)]


print("==== Enter 'exit' to quit this app. ====")

while True:
    
    fullname = input('Enter your name:')        

    blank1 = ' ' in fullname
    blank2 = '　' in fullname
    
    if fullname == 'exit':
        break  

    if blank1 == True or blank2 == True:
        print('---- It\'s written properly. ----')

    if len(fullname) == 2:
       last = fullname[0:1]
       first = fullname[1:]
       space = " "
       print(last + space + first)
    else:
        if __name__ == "__main__":
            
            name_pattern = name_patterns(fullname)  #姓名の全分割パターンを格納
            appl_data = kanji_search(fullname)  #漢字ファイルの読み込み、該当する漢字を抽出
            each_oPoint = o_point(appl_data,fullname)   #Order pointの計算
            each_lPoint = l_point(appl_data,fullname)   #Length pointの計算
            print(judge(each_lPoint,each_oPoint,fullname))  #正しい分割方法を判定、結果出力

        print('---- next ----')