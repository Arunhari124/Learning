import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df=pd.read_csv("country_wise_latest.csv")
report=[df["Confirmed"].sum(),df["Recovered"].sum(),df["Deaths"].sum()]
valu=["confirmed",'recovered','death']
#line_plot=sns.lineplot(x=valu,y=report)
plt.bar(valu,report)
#print(df.head())
plt.show()