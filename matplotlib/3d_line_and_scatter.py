import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import random

fig = plt.figure()
ax1=fig.add_subplot(111, projection='3d')

x = [a for a in range(10)]
y = random.sample(range(0, 10), 10)
z = random.sample(range(0, 10), 10)

# 3d line chart
ax1.plot(x, y, z)

# 3d scatter chart
ax1.scatter(x, y, z, color='r')

ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')

plt.show()