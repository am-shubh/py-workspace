import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import random
import numpy as np

fig = plt.figure()
ax1=fig.add_subplot(111, projection='3d')

x = [a+1 for a in range(10)]
y = random.sample(range(0, 10), 10)
z = np.zeros(10)

depthX = np.ones(10)
depthY = np.ones(10)
depthZ = [a+1 for a in range(10)]

ax1.bar3d(x, y, z, depthX, depthY, depthZ)

ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')

plt.show()

