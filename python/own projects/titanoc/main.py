import pandas as pd
import numpy as np

df=pd.read_csv("titanic.csv")

#How many passengers?
passengers_no=(df["Survived"]).count()
#How many males?
male=df[df["Sex"]=="male"]["PassengerId"].count()
#How many females?
female=df[df["Sex"]=="female"]["PassengerId"].count()
#Oldest passenger?
old_age=df["Age"].max()
#Youngest passenger?
young_age=df["Age"].min()
#Passengers in class 1?
pclass1=df[df["Pclass"]==1]["PassengerId"].count()
#Passengers in class 2?
pclass2=df[df["Pclass"]==2]["PassengerId"].count()
#Passengers in class 3?
pclass3=df[df["Pclass"]==3]["PassengerId"].count()
#Average fare?
avg_fare=df.groupby("Sex")["Fare"].mean()
print(df["Sex"].value_counts())
print(df.describe())
print(male)








#print(avg_fare)
