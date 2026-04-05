import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 4, 1, 5, 7, 3, 6, 8])

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', marker='o')

# Labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Scatter Plot")

plt.grid(True)
plt.show()
