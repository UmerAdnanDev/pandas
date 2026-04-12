import pandas as pd
data ={
  "Name":[None,"Rizwan","Usoof","Jamal"],
  "Age":[24,23,None,28],"Salary":[100000,120000,95000,None]
  ,"Experience":[None,1.5,1,2]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())