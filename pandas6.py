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
# with condition
print("Employee with 1 yr + experience")
print(df[df["Experience"] > 1 ])
# multi conditions
print("Employee with 100k <= salary and Age > 25")
e1 = df[(df["Salary"] >= 100000) & (df["Age"] >= 25)]
print(e1)
print("Employee with 100k <= salary or Age > 25")
e2 = df[(df["Salary"] >= 100000) 
        | (df["Age"] >= 25)]
print(e2)