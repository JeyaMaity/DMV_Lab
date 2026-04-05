import matplotlib.pyplot as plt
import numpy as np

x=list(map(int,input("Enter values:").split()))
y=list(map(int,input("Enter values:").split()))

plt.hist(y, bins=x, edgecolor="black")

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("dynamic histogram")
plt.show()
