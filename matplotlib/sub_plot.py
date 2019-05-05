import matplotlib.pyplot as plt
import random

fig = plt.figure()

def get_data():
	# x and y values to plot
	x = [a for a in range(10)]
	y = random.sample(range(0, 10), 10)

	return (x, y)

# subplot method
# plt.subplot(2, 1, 1)
# plt.plot(x, y, label='subplot1')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()

# plt.subplot(2, 1, 2)
# plt.plot(x, y, label='subplot2')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()


# add subplot method
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(212)

# (x, y) = get_data()
# ax1.plot(x, y)

# (x, y) = get_data()
# ax2.plot(x, y)

# (x, y) = get_data()
# ax3.plot(x, y)


# subplot2grid method
ax1 = plt.subplot2grid((8, 1), (0,0), rowspan=2, colspan=1)
ax2 = plt.subplot2grid((8, 1), (2,0), rowspan=4, colspan=1)
ax3 = plt.subplot2grid((8, 1), (6,0), rowspan=2, colspan=1)

(x, y) = get_data()
ax1.plot(x, y)

(x, y) = get_data()
ax2.plot(x, y)

(x, y) = get_data()
ax3.plot(x, y)

plt.show()