import pandas as pd

df=pd.read_csv("titanic.csv")

#survivers_list=df[df["Survived"]==1]
#print(survivers_list)
#print(df)
#cabin=df.dropna(subset=["Cabin"])
#print(cabin)
#df=df.fillna({"Cabin":"Outside"})
#print(df)
#df["Survived"]=df["Survived"].replace({0:"DIEd",1:"Alive"})
#print(df)
#df["Name"]=df["Name"].str.upper()
#print(df.to_string)
#age_mean=df["Age"].mean()
#print(age_mean)
#age_btw=df[(df["Age"] >= 20) & (df["Age"] <=29)]
#print(age_btw.to_string())
#fem=df["Sex"].value_counts()
#print(fem)
#avg=df[df["Sex"] == "male"]["Age"].mean()
#print(avg)\
#avg_fem=df[df["Sex"]=="female"]["Age"].mean()
#print(avg_fem)
#count_of_survi=df["Survived"].count()
#print(count_of_survi)
#age_max=df["Age"].max()
#print(age_max)
#age_min=df["Age"].min()
#print(age_min)
sur=df.groupby("Sex")["Survived"].mean()
print(sur)