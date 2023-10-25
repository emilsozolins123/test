import pandas as pd 

fails = pd.read.csv('data.csv')
info_list = fails.values.tolist()
saraksts = []

for i in range (len(info_list)):
    if info_list [i][1] == "A105900":
        saraksts.append(info_list[i][4])
        
        rezultats = sum(saraksts)/len(saraksts)
        
        print(rezultats)