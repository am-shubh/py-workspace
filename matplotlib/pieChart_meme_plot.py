import matplotlib.pyplot as plt

slices = [1, 2, 4, 3]
description = ['The information', 'Team work', 'How to do things on my own', 'How much I hate people']
colors = ['c', 'g', 'y', 'r']

plt.pie(slices, 
	labels=description, 
	colors=colors, 
	startangle=90,
	autopct='%1.1f%%')

plt.title('What I learn from group projects')

plt.show()
