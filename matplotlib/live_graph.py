import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig = plt.figure()

# font properties that will be put on plot
fontDict = {
	'family': 'serif',
	'color': 'darkred',
	'size': 15
}

def animate(i):
	x, y = np.loadtxt('data/example.txt', delimiter= ' ', unpack=True)

	# clearing plot to replot new values
	fig.clear()

	plt.plot(x, y, label='Live Data')

	# to put texton plot
	plt.text(8, 8 ,'Live Plotting', fontdict = fontDict)

	plt.xlabel('X Values')
	plt.ylabel('Y Values')
	plt.title('Live Data Plotting from example.txt file')
	plt.legend()


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()