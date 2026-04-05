import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Corrected data
x = np.arange(0, 10, 1)
y = np.array([1, 3, 2, 5, 4, 6, 5, 7, 6, 8])

fig, ax = plt.subplots()

# Fix axis limits to match your data
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    line.set_data(x[:frame], y[:frame])  # Draw progressively
    return line,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(x) + 1,
    init_func=init,
    interval=500,
    blit=True
)

plt.title("animated line")

plt.show()
