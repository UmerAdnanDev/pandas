import pandas as pd
data ={
  "Name":["Sameer","Rizwan","Usoof","Jamal"],
  "Age":[24,23,26,28],"Salary":[100000,120000,95000,150000]
  ,"Experience":[1,1.5,1,2]
}
df = pd.DataFrame(data)
print(df)
# Updating Values 
df.loc[1,"Age"] = 25 # individually
print(df)
df["Salary"] = df["Salary"] * 1.1 # 10% hike
print(df)