import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Sample Data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 4, 1, 5, 7, 3, 6, 8])

fig, ax = plt.subplots(figsize=(8, 5))

ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_title("Animated Scatter Plot")
ax.grid(True)

scatter = ax.scatter([], [], color='blue')

def animate(frame):
    scatter.set_offsets(np.c_[x[:frame], y[:frame]])
    return scatter,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(x) + 1,
    interval=500,
    blit=True,
    repeat=False
)

plt.show()
