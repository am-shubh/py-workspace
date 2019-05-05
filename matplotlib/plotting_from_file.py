import matplotlib.pyplot as plt

# with csv
'''
import csv

x = []
y = []

with open('data/example.txt', 'r') as file:
	plots = csv.reader(file, delimiter=' ')

	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

'''

# with numpy
import numpy as np

# getting x and y values from file
x, y = np.loadtxt('data/example.txt', delimiter= ' ', unpack=True)


plt.plot(x, y, label = 'Plotting from file')

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Plotting From file')
plt.legend()

plt.show()