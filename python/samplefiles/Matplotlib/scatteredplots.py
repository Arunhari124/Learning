import matplotlib.pyplot as plt

x=[0,1,1,2,3,4,5,6,7,7,8]
y=[55,60,65,63,68,70,75,78,82,85,87]

plt.scatter(x,y,color="Skyblue",
            alpha=0.6,
            s=200)
plt.title("test scores")
plt.xlabel("hours studied")
plt.ylabel("grades")
plt.show()