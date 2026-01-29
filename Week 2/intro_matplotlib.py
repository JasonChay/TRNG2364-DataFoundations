# Library for creating static, animated, interactive visualizations
# Provides an API that is object-oriented for embedding plots into applications
# using general GUI kits like TKinter, wxPython, Qt, or GTK

import matplotlib.pyplot as plt

# Creating a line plot
x = [1, 2, 4, 6, 8]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.title("My Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()



# Creating a bar chart
categories = ["Fruits", "Vegetables", "Meat", "Dairy"]
values = [8, 11, 4, 6]

plt.bar(categories, values, color="g")
plt.title("Food in My Pantry")
plt.xlabel("Food Categories")
plt.ylabel("Number of Items")
plt.show()



# Creating a scatter plot
x_scatter = [9, 81, 43, 66, 12, 9]
y_scatter = [100, 5, 45, 25, 49, 8]

plt.scatter(x_scatter, y_scatter, color='r')
plt.title("My Scatter Plot")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()