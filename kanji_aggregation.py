import numpy as np
import pandas as pd
import csv

def split_fullname(filepath):


    kanji_data = pd.read_csv(filepath, header=None)
    kanji_array = np.array
    kanji_array = kanji_data.values
    print(kanji_array)
    count = kanji_array.shape[0]
    print(kanji_data)

    for i in range(count):
        fullname = kanji_array[i]
        print(fullname)
        position = np.where([fullname == " "])
        print(position)
        surname = [] 
        surname.append(fullname[:position])
        given_name = []
        surname.append(fullname[len(fullname) - position:])
        print(surname)
        print(given_name)

        


#    kanji_array.find(' ') #半角

#    [0][]



def analyze_names(parameter_list):
    a = 0

def insert(parameter_list):
    b = 0



filepath = input("File path:")


if __name__ == "__main__":
    split_fullname(filepath)


