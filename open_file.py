import pandas as pd
from parse import *

# getting id from table file
def take_list_from_file():
    File_exel = pd.read_excel("./table.xlsx")
    imtId_list_durty = File_exel.values.tolist()
    imtId_list_clear = []
    for item in imtId_list_durty:
        imtId_list_clear.append(int(str(item).replace("[", "").replace("]", "")))
    return imtId_list_clear
