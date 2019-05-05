import matplotlib.pyplot as plt

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# 8 hours of day spend online doing following
youtube = [4, 2, 3, 1, 2, 3, 4]
facebook = [2, 1, 2, 2, 2, 2, 1]
learning = [2, 5, 3, 5, 4, 3, 3]

plt.stackplot(days, youtube,facebook,learning, labels=['youtube', 'facebook', 'learning'], colors=['m','r','c'])

plt.xlabel('Days')
plt.ylabel('# of hours')
plt.title('8 hours of each day')

plt.legend()
plt.show()