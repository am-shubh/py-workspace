import numpy as np
import time
import sys

'''
comparing for size
'''

# list 0 to 999 i.e. [0, 1000)
list_ = list(range(1000))

# defining same type list in numpy
numpyArr = np.arange(1000)

'''
to get space occupied by the 'list_'
get any numer between 0 and 1000, it will give size of one element
multiply that with size of list_

for numpy we can use itemsize and size
'''

# print('Size of one element in python List :: ', sys.getsizeof(5))
# print('Size of one element in Numpy array :: ', numpyArr.itemsize)

print('size of python List = ', sys.getsizeof(5)*len(list_))
print('size of numpy array = ', numpyArr.size * numpyArr.itemsize)

'''
comparing for time or speed
defining two list and two array and comparing time for their addition
'''

list1_ = list(range(100000))
list2_ = list(range(100000))

numpyArr1 = np.arange(100000)
numpyArr2 = np.arange(100000)

# calculating time for adding two lists
startTime = time.time()
resultList = [(x + y) for x, y in zip(list1_, list2_)]
timeTaken = time.time() - startTime
print('time taken to add two list = ', timeTaken * 1000)

# calculating time for adding two numpy arrays
startTime = time.time()
resultArray = numpyArr1 + numpyArr2
timeTaken = time.time() - startTime
print('time taken to add two numpy array = ', timeTaken * 1000)










 