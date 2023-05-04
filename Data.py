import pandas as pd
import numpy as np

from glob import glob

if __name__ == "__main__":
    files = glob("./data/**/**/*")
    df_list = []
    for file in files:
        file_st = file.split("\\")[-1].split("-")
        date = file_st[0]
        plate = file_st[1]
        temp_df = pd.read_fwf(file, encoding="cp949", skiprows=1, headers=)
        temp_df[date] = date
        temp_df[plate] = plate
        temp_df.colums
        
        pd.read_excel("./data/origin/o2019년_a.xlsx", skiprows=2)

