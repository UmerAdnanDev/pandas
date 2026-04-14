import pandas as pd
data1 ={
  "Name":[None,"Rizwan","Usoof","Jamal"],
  "Age":[24,23,None,28],"Salary":[100000,120000,95000,None]
  ,"Experience":[None,1.5,1,2]
}
df1 = pd.DataFrame(data1)
print(df1)
df1.fillna(0,inplace=True)
print(df1)
data2 ={
  "Name":["Ahmed","Rizwan","Usoof","Jamal"],
  "Age":[24,23,None,28],"Salary":[100000,120000,95000,None]
  ,"Experience":[None,1.5,1,2]
}
df2 = pd.DataFrame(data2)
'''This use of inplace will deprecate in new version'''
# df2["Age"].fillna(df2["Age"].mean(),inplace=True) # replaces the value with mean (average)
# df2["Salary"].fillna(df2["Salary"].mean(),inplace=True)
# df2["Experience"].fillna(df2["Experience"].mean(),inplace=True)
df2["Age"] = df2["Age"].fillna(df2["Age"].mean())
df2["Salary"] = df2["Salary"].fillna(df2["Age"].mean())
df2["Experience"] = df2["Experience"].fillna(df2["Experience"].mean())
print(df2)