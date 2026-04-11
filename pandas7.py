import pandas as pd
data ={
  "Name":["Sameer","Rizwan","Usoof","Jamal"],
  "Age":[24,23,26,28],"Salary":[100000,120000,95000,150000]
  ,"Experience":[1,1.5,1,2]
}
df = pd.DataFrame(data)
print(df)
#Addinng column
df["Bonus"] = df["Salary"] * 0.1
print(df)
df.insert(0,"ID",[1,2,3,4])