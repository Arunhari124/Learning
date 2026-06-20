import pandas as pd

df=pd.read_csv("data.csv",index_col="Name")

#selection by colum
#print(df["Name"].to_string())
#heiht
#print(df["Height"].to_string())
#weight
#print(df["Weight"].to_string())
#print(df[["Name","Height","Weight"]].to_string())


#selection by row

#print(df.loc["Blastoise":"Mewtwo",["Height","Weight"]])
#print(df.iloc[0:11:2,0:3])

pokemon=input("Enter a pokemon name: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(F"{pokemon} not found ")