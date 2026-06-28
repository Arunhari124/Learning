import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("student.csv")
barcart=sns.barplot(x=df['name'],y=df["career"],palette="muted")
plt.show()