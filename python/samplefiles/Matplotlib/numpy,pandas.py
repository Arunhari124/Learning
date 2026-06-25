import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("titanic.csv")
type_count=df["Sex"].value_counts(ascending=True)
plt.bar(type_count.index,type_count.values,color="green",edgecolor="Black")
plt.title("gender")
plt.show()