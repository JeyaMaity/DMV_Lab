import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Data
categories = ['Python', 'Java', 'C++', 'JavaScript']
values = np.array([40, 25, 20, 15])

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(categories, [0]*len(values),
              color=['gold', 'lightblue', 'lightgreen', 'coral'])

ax.set_ylim(0, max(values) + 10)
ax.set_xlabel("Programming Languages")
ax.set_ylabel("Popularity")
ax.set_title("Programming Language Popularity")

def animate(frame):
    progress = frame / 100
    for bar, value in zip(bars, values):
        bar.set_height(value * progress)
    return bars

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=101,
    interval=30,
    blit=False,
    repeat=False
)

plt.show()
