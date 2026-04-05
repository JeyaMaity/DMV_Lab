import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,15,25,30]

plt.plot(x,y,marker='o')

plt.xlabel("x values (Independent variable)")
plt.ylabel("Y values (Dependent variable)")

plt.title("X-Y Axis data Plot")

plt.grid(True)

plt.show()
