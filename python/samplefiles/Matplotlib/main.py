import matplotlib.pyplot as plt
import numpy as np


x=np.array([1,2,4,5,6])
y=np.array([1,3,2,3,1])
z=np.array([2,4,3,4,2])
z1=np.array([3,5,4,5,3])
dict1=dict(marker="o",markersize=10,markerfacecolor="green",
         markeredgecolor="red",linestyle="dotted",
         color="red")

plt.title("Class size",fontsize=20,family="Arial",fontweight="bold",color="blue")
plt.xlabel("Year",fontsize=20,family="Arial",fontweight="bold",color="yellow")
plt.ylabel("food",fontsize=20,family="Arial",fontweight="bold",color="yellow")
plt.plot(x,y, **dict1)
plt.plot(x,z,**dict1)
plt.plot(x,z1,**dict1)
#plt.xticks(x)
#plt.tick_params(axis="both",colors="black")
plt.show()