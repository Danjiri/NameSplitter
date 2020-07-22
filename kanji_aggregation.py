import numpy as np
import pandas as pd
import csv

def split_fullname(filepath):

    quote = '"'
    filepath = quote + filepath + quote
    kanji_data = pd.read_csv(filepath, header=None)
    kanji_array = np.array
    kanji_array = kanji_data.values

def analyze_names(parameter_list):
    pass

def insert(parameter_list):
    pass



filepath = input("File path:")


if __name__ == "__main__":
    split_fullname(filepath)


