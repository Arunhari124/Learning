import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("titanic.csv")
figure,axes=plt.subplots(2,2)

df["Age"].hist(ax=axes[0,0])
axes[0,0].set_title("Age Distribution")
axes[0,0].set_xlabel("Age")
axes[0,0].set_ylabel("Passengers")
survival_counts=df["Survived"]=df["Survived"].replace({0:"DIEd",1:"Alive"}).value_counts()
axes[0,1].bar(survival_counts.index,survival_counts.values,color=["green","red"],edgecolor="black")
axes[0,1].set_xlabel("Status")
axes[0,1].set_ylabel("Count")


axes[0,1].set_title("Survival rate")


gender_counts=df["Sex"].value_counts()
axes[1,0].bar(gender_counts.index,gender_counts.values,color=["Blue","pink"],edgecolor="black")
axes[1,0].set_title("Gender")

class_counts=df["Pclass"].value_counts()
x=axes[1,1].bar(class_counts.index,class_counts.values,color=["Black","yellow","#cfe3d0"])
plt.bar_label(x, labels=["1", "2","3"])
axes[1,1].set_title("Pclass")

plt.tight_layout()
plt.show()