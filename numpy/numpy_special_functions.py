import numpy as np
import matplotlib.pyplot as plt

sine function plotting
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)

# cos function plotting
x = np.arange(0, 3*np.pi, 0.1)
y = np.cos(x)

# tan function plotting
x = np.arange(0, 3*np.pi, 0.1)
y = np.tan(x)

plt.plot(x, y)
plt.show()

# exponential function
ar = np.array([1, 2, 3])
print(np.exp(ar))

# logarithmic function
print(np.log(ar))		# natural log or ln funct
print(np.log10(ar))		# log to base 10
