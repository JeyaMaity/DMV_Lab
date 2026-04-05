import matplotlib.pyplot as plt
import numpy as np

x=list(map(int,input("Enter values:").split()))
y=list(map(int,input("Enter values:").split()))

x= np.array(x)
y=np.array(y)

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Static Line Chart")
plt.show()
