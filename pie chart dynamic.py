import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = np.array([40, 25, 20, 15])
colors = ['gold', 'lightblue', 'lightgreen', 'coral']

fig, ax = plt.subplots(figsize=(6, 6))
ax.axis('equal')

# Create initial empty pie
wedges, texts, autotexts = ax.pie(
    [0]*len(sizes),
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90
)

ax.set_title("Programming Language Popularity")

def init():
    for wedge in wedges:
        wedge.set_theta1(90)
        wedge.set_theta2(90)
    return wedges

def animate(frame):
    total = sum(sizes)
    cumulative = np.cumsum(sizes)
    
    for i, wedge in enumerate(wedges):
        start_angle = 90 + (cumulative[i-1] / total * 360 if i > 0 else 0)
        end_angle = 90 + (cumulative[i] / total * 360)
        
       
        progress = frame / 100
        wedge.set_theta1(90)
        wedge.set_theta2(90 + (end_angle - 90) * progress)
        
    return wedges

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=101,
    init_func=init,
    interval=30,
    blit=False,
    repeat=False
)

plt.show()
