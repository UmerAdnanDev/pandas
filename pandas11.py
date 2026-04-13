
import pandas as pd
data1 ={
  "Name":[None,"Rizwan","Usoof","Jamal"],
  "Age":[24,23,24,28],"Salary":[100000,120000,95000,150000]
  ,"Experience":[1,1.5,1,2]
}
df1 = pd.DataFrame(data1)
print(df1)
df1.dropna(inplace=True) # row removed axis = 0 by defaut
print(df1)
data2 ={
  "Name":["Saim","Rizwan","Usoof","Jamal"],
  "Age":[24,23,24,28],"Salary":[100000,None,95000,150000]
  ,"Experience":[1,1.5,1,2]
}
df2 = pd.DataFrame(data2)
print(df2)
df2.dropna(axis=1,inplace=True) # column removed axis = 1 
print(df2)