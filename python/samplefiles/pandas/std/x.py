import pandas as pd

df=pd.read_csv("titanic.csv")

print(df.shape[0])#rows
print(df.shape[1])#colums
print(df.columns)#prints all colum names
print(df.isnull().sum())