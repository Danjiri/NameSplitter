import numpy as np
import pandas as pd
import csv

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
    