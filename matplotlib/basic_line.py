import matplotlib.pyplot as plt

# defining x and y points
x1 = [0, 1, 2, 3, 4]
y1 = [1, 5, 3, 0, 2]

x2 = [0, 1, 2, 3, 4]
y2 = [3, 4, 0, 6, 1]

# plotting and displaying
plt.plot(x1, y1, label='Line1')
plt.plot(x2, y2, label='Line2')

# defining labels on x and y axis
plt.xlabel('X values')
plt.ylabel('Y values')

# title of graph
plt.title('Basic Line Plots')

# adding legend to plot
plt.legend()

# displaying the plot
plt.show()