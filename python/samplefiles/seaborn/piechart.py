import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv("student.csv")
name=df['name']
salary=df["career"]
plt.pie(salary,labels=name,autopct="%1.1f%%")
plt.show()