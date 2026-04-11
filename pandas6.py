import pandas as pd
data ={
  "Name":["Sameer","Rizwan","Usoof","Jamal"],
  "Age":[24,23,26,28],"Salary":[100000,120000,95000,150000]
  ,"Experience":[1,1.5,1,2]
}
# Filtering by Columns
df = pd.DataFrame(data)
print(df)
print("1 column") # series
print(df["Experience"])
print("2 column")# data frame
print(df[["Name","Salary"]])
