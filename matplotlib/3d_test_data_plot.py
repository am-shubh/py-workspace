import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax1=fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()

ax1.plot_wireframe(x, y, z, rstride=1, cstride=0)

ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')

plt.show()

