import matplotlib.pyplot as plt
import numpy as np

categories=np.array(["Freshman","Sophomores","juniors","Seniors"])
values=np.array([300,250,275,225])
colors=["red","green","blue","black","yellow"]

plt.pie(values,labels=categories,
        autopct="%1.1f%%",colors=colors
        ,explode=[0,0,0,0.2],
        shadow=True,
        startangle=180)
plt.title("My college")

plt.show()