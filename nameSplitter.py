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

        #OrderPointの計算

     #OrderPointの計算
  

    for i in range(1,len(fullname)-2): 

        if i == 1:  #2文字目の各パターンの確率                        
            for j in reversed(range(2,5)):#1の全パターン                 
                appl_data[i][j] / (appl_data[i][2] + appl_data[i][3] + appl_data[i][4])                
        else:
               #それ以外の各パターンの確率
            for k in reversed(range(3,5)):
                print(k)
                if i : 
                for l in range(i-1):
                    print(l)                
                    appl_data[i][5] / (appl_data[i][2] + appl_data[i][3] + appl_data[i][4] + appl_data[i][5])
                appl_data[i][l] / (appl_data[i][2]  + appl_data[i][3] + appl_data[i][4] + appl_data[i][5])


"""

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
        appl_data[2][4] / (appl_data[2][2] + appl_data[2][3] + appl_data[2][4] + appl_data[2][5]) #敦 3

        appl_data[i][5 - (1~3, 0~3)] /(appl_data[i][2] + appl_data[i][3] + appl_data[i][4] + appl_data[i][5])
        appl_data[i][5 - (1~3, 0~3)] /(appl_data[i][2] + appl_data[i][3] + appl_data[i][4] + appl_data[i][5])
###        
"""


"""
        #LengthPointの計算
    for 


        #1
        appl_data[0][7] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9])    #坂
        appl_data[1][13] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])       #本
        appl_data[2][13] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])      #敦
        appl_data[3][13] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13])     #史

        #2
        appl_data[0][8] / (appl_data[0][7] + appl_data[0][8] + appl_data[0][9])  #坂
        appl_data[1][8] / (appl_data[1][8] + appl_data[1][9] + appl_data[1][13])   #本            
        appl_data[2][13] / (appl_data[2][9] + appl_data[2][12] + appl_data[2][13])  #敦
        appl_data[3][13] / (appl_data[2][11] + appl_data[2][12] + appl_data[2][13]) #史    

        #3
        appl_data[][] / appl_data[][] + appl_data[][] + appl_data[][]

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
