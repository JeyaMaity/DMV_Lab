import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)


fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x, y1, color='blue')
axs[0].set_title("Sine Wave")
axs[0].set_xlabel("x")
axs[0].set_ylabel("sin(x)")


axs[1].plot(x, y2, color='red')
axs[1].set_title("Cosine Wave")
axs[1].set_xlabel("x")
axs[1].set_ylabel("cos(x)")

plt.tight_layout()
plt.show()
