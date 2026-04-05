import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Data setup
x = np.linspace(0, 2*np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)


fig, axs = plt.subplots(1, 2, figsize=(10, 4))


line1, = axs[0].plot([], [], 'b-')
line2, = axs[1].plot([], [], 'r-')


axs[0].set_title("Dynamic Sine Wave")
axs[0].set_xlim(0, 2*np.pi)
axs[0].set_ylim(-1, 1)

axs[1].set_title("Dynamic Cosine Wave")
axs[1].set_xlim(0, 2*np.pi)
axs[1].set_ylim(-1, 1)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


def update(frame):
    # Animate by shifting phase
    line1.set_data(x, np.sin(x + 0.1*frame))
    line2.set_data(x, np.cos(x + 0.1*frame))
    return line1, line2


ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

plt.tight_layout()
plt.show()
