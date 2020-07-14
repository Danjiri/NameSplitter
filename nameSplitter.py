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

