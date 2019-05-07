import numpy as np

# two dim array
a = np.array([
		(1, 2, 3, 7), 
		(4, 5, 6, 8)
	])

print("Original array = \n", a)

# printing dimensions of numpy array
print("Dimension = ", a.ndim)

# size of each element
print("Item size = ", a.itemsize)

# data type of elements
print("data type = ", a.dtype)

# size of numpy array i.e. no. of elements
print("No. of elements = ", a.size)

# shape of array i.e. rows X cols
print("shape of array = ", a.shape)


# --------------------------------------------------------------------------------

# reshaping arrays i.e. changing rows and cols
print('[INFO] Reshaping array')
b = a.reshape(4, 2)
print("Reshaped array = \n", b)
print("Reshaped array size = ", b.shape)


# --------------------------------------------------------------------------------

# Line spacing
# 5 numbers between 1 and 4, equally placed
x = np.linspace(1, 4, 5)
print(x)


# --------------------------------------------------------------------------------

# max no. in array
print("Max no. in array = ", a.max())

# min no. in array
print("Min no. in array = ", a.min())

# sum of elements in array
print("Sum of elements in array = ", a.sum())


# --------------------------------------------------------------------------------

# rows in numpy array are called 'axis1' and cols are called 'axis0'

# to get sum of elements in rows
print("Sum of rows elements = ", a.sum(axis = 1))

# to get sum of elements in rows
print("Sum of cols elements = ", a.sum(axis = 0))


# --------------------------------------------------------------------------------

# Square root
print("Square root of array = \n", np.sqrt(a))

# standard deviation
print("Standard deviation = ", np.std(a))


# --------------------------------------------------------------------------------

# slicing array

# printing single element
print(a[0, 2])		# 1st row and 3rd elem

# printing particular elem of every row
print(a[0:, 3])		# 4rd elem of every row

# Therefore print(a[0:2, 3]) means 3rd elem from 1st to 2nd row. '2' is exclusive


# --------------------------------------------------------------------------------

y = np.array([
		(5, 8, 1, 2),
		(9, 0, 7, 3)
	])

# addition of two arrays
print("Addition of two arrays\n", a + y)

# subtraction of two arrays
print("subtraction of two arrays\n", a - y)

# multiplication of two arrays
print("Multiplication of two arrays\n", a * y)

# Division of two arrays
print("Division of two arrays\n", a / y)


# --------------------------------------------------------------------------------

# concatenation of two arrays

# Vertical stacking
print(np.vstack((a, y)))

# Horizontal stack
print(np.hstack((a, y)))


# --------------------------------------------------------------------------------

# converting array into single column
print(a.ravel())