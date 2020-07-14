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
                

    print(appl_data[0][0])

    print(appl_data[0][1])
    print(appl_data[0][14])

    evaluated_data = []

#    for i in range(len(fullname)):
#        for l in range(1,14):
#            order_point = appl_data[i][l]
#            length_point = 
#    surname
#    name  [][]+[][] /(len(fullname) - 1)







  






print("==== Enter 'exit' to stop this app. ====")

while True:
    
    name = input('Enter your name:')        

    blank1 = ' ' in name
    blank2 = '　' in name
    
    if name == 'exit':
        break  

    if blank1 == True or blank2 == True:
        print('---- It\'s written properly. ----')
    else:
        main(name)    
        print('---- next ----')

