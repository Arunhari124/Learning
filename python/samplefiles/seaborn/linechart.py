import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv("student.csv")

line_plot=sns.lineplot(x=df["id"],y=df["career"])
line_plot.set_title("AGe by nAme")
line_plot.set_xlabel("name")
line_plot.set_ylabel("Age")
plt.show()


