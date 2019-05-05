import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [5, 9, 3, 1, 4, 6, 10, 2, 8, 12]
y2 = [4, 6, 2, 0, 7, 8, 3, 1, 10, 9]


plt.scatter(x, y1, label='Scatter1', color='k', marker='*')
plt.scatter(x, y2, label='Scatter2', color='c')

plt.xlabel('X values')
plt.ylabel('Y values')

plt.title('Scatter Plot')

plt.legend()

plt.show()

