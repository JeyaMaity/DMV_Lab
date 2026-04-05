import matplotlib.pyplot as plt

# Data
categories = ['pekachu', 'squrtle', 'charizard', 'bulbasaur']
values = [40, 25, 20, 15]

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['gold', 'lightblue', 'lightgreen', 'coral'])

# Labels and title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Favourite Pokemon ")

plt.show()
