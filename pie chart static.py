import matplotlib.pyplot as plt


labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['gold', 'lightblue', 'lightgreen', 'coral']


plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',  
    startangle=90        
)

plt.title("Programming Language Popularity")
plt.axis('equal')  

plt.show()
