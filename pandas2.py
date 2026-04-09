import pandas as pd 
# head() and tail() by defaul will give first 5 / last 5 rows
df = pd.read_csv("data0.csv")
print("1st 3 rows")
print(df.head(3)) # 1st 3 rows
print()
print("Last 3 rows")
print(df.tail(3)) #last 3 rows  