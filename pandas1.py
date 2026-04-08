import pandas as p
data1 = {
  "Name":['Umer','Khizar','Saad','Ebad'],
  "Age":[19,18,18,17],
   "Studying":["BSE","BSE","CMA","CA"],
   "Institute":["SSUET","SSUET","ICMA","?!"]
}
data2 = {
  "Roll":[101,432,253,412,335],
  "Name":["Sami","Raza","Sameer","Nabeel","Ahmed"],
  "Age":[19,23,21,26,27]
}
df1 = p.DataFrame(data1)
df2 = p.DataFrame(data2)
print(df1)
print()
print(df2)
# creates data in certain file formate
df1.to_csv("data1.csv",index=False)#index will be removed
df1.to_excel("data1.xlsx",index=False)
df2.to_json("data2.json",index=False)
df2.to_excel("data2.xlsx",index=False)