import numpy as np
import pandas as pd
import csv
import lpoint
import opoint


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

    name_pattern = []
    for i in range(1,len(fullname)):
        #考えられる名前分割パターンの全通り
        tmp_lastname = fullname[0:i]
        tmp_firstname = fullname[i:]
        space = " "
        name_pattern.append(tmp_lastname + space + tmp_firstname)
        
    


    #OrderPointの計算  
    each_oPoint = opoint.o_point(appl_data,fullname)
    #LengthPointの計算
    each_lPoint = lpoint.l_point(appl_data,fullname)

#    print(each_oPoint)
#    print(each_lPoint)

    #判定
    judge_name = []
    for i in range(0,len(fullname) - 1):
        judge_name.append(each_lPoint[i] + each_oPoint[i])
    
    print(name_pattern[np.argmax(judge_name)])
  


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
