import matplotlib.pyplot as plt
import random

# sample data for histogram
population_ages = random.sample(range(1, 100), 75)

# defining bins of range 10
bins = [x for x in range(0, 110, 10)]

# plotting histogram
plt.hist(population_ages, bins, histtype='bar', rwidth=0.9)

# defining labels on x and y axis
plt.xlabel('Age Group')
plt.ylabel('# of people')

# title
plt.title('Population age')

# displaying the plot
plt.show()


