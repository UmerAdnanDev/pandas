import pandas as pd
df_csv = pd.read_csv("data0.csv") # encoding latin1 or utf-8   pd.read_csv("data0.csv",encoding = "latin1")
print(df_csv)
df_json = pd.read_json("data0.json")
print(df_json)
df_txt =  pd.read_csv("data0.txt",sep="|")
print(df_txt)
df_excel =  pd.read_excel("data1.xlsx")
print(df_excel)

