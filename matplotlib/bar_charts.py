import matplotlib.pyplot as plt

# defining x and y points
x1 = [0, 2, 4, 6, 8]
y1 = [1, 5, 3, 0, 2]

x2 = [1, 3, 5, 7, 9]
y2 = [3, 4, 2, 6, 1]

plt.bar(x1, y1, label="Bar1")
plt.bar(x2, y2, label="Bar2")

# defining labels on x and y axis
plt.xlabel('X values')
plt.ylabel('Y values')

# title of graph
plt.title('Bar Graphs')

# adding legend to plot
plt.legend()

# displaying the plot
plt.show()