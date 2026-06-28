import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv("student.csv")
data=df["age"],df["career"]
scp=sns.heatmap(data)
scp.set_title("nigha")
scp.set_xlabel("bigg")
scp.set_ylabel("mmmm")
plt.show()