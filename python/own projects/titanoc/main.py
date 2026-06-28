import pandas as pd
import numpy as np

df=pd.read_csv("titanic.csv")

#How many passengers?
passengers_no=(df["Survived"]).count()
       #891
#How many males?
male=df[df["Sex"]=="male"]["PassengerId"].count()
       #577
#How many females?
female=df[df["Sex"]=="female"]["PassengerId"].count()
      #314
# Average age by gender
avg_age=df.groupby("Sex")["Age"].mean()
   #female=27.915709
   #male=30.726645
#Oldest passenger?
old_age=df["Age"].max()
#80
#Youngest passenger?
young_age=df["Age"].min()
#0.42
#Passengers in class 1?
pclass1=df[df["Pclass"]==1]["PassengerId"].count()
#216
#Passengers in class 2?
pclass2=df[df["Pclass"]==2]["PassengerId"].count()
#184
#Passengers in class 3?
pclass3=df[df["Pclass"]==3]["PassengerId"].count()
#491
#Average fare?
avg_fare=df.groupby("Sex")["Fare"].mean()
#female    44.479818
#male      25.523893
#average age by class
avg_class_age=df.groupby("Pclass")["Age"].mean()
#1    38.233441
#2    29.877630
#3    25.140620
# Survival rate by gender
survival_gen=df.groupby("Sex")["Survived"].mean()
#female    0.742038
#male      0.188908
# Survival rate by class
survival_pclass=df.groupby("Pclass")["Survived"].mean()
#1    0.629630
#2    0.472826
#3    0.242363
#all gender stats
gen_stts=df["Sex"].value_counts()
#male      577
#female    314
print(df.describe())
