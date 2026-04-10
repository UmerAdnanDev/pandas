import pandas as pd
data ={
  "Name":["Sameer","Rizwan","Usoof","Jamal"],
  "Age":[24,23,26,28],"Salary":[100000,120000,95000,150000]
}
df = pd.DataFrame(data)
print("Sample Employee Data")
print(df)
print("Descriptive Statistics")
print(df.describe())


