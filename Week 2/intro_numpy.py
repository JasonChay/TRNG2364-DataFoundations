# library for numerical computing
# support for arrays, matricies, and a wide range of 
# mathematical functions to operate on these data structures
# many libraries build on top of numpy
# pandas, scipy, scikit-learn

# numpy is written in C and Fortran, making it very fast for computations

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 5, 6, 34, 81]) # initializing with a list
print("1D array: ", array_1d)

# Create a 2D array
array_2d = np.array([[5, 9, 18], [91, 45, 16]])
print("2D array: \n", array_2d)

# Perform some basic operations

# Addition
array_sum = array_1d + 10
print("Array after addition: ", array_sum)

# Multiplication
array_product = array_1d * 4
print("Array after multiplication: ", array_product)

# Calculate the mean
mean = np.mean(array_1d)
print("Mean: ", mean)

# Calculate standard deviation
stdev = np.std(array_1d)
print("Standard Deviation: ", stdev)

# Reshape our 1d array to 2d array
reshaped_array = array_1d.reshape((3, 2))
# reshaped_array = np.reshape(array_1d, (6, 1))
print("Reshaped Array: ", reshaped_array)

# Access elements
print("Element in 0 index: ", array_1d[0])
print("Element in 0,0 index for 2D array: ", array_2d[0][0])



# More numpy notes
print()
print("More Numpy")
arr = np.array([10, 15, 20, 25, 30])

# Boolean indexing
print(arr[arr > 20])

# Fancy indexing
# aka Advanced indexing uses a list of indices to access elements of an array
indices = [0, 2, 4]
print(arr[indices])
# alternatively integer array indexing
print(arr[[0, 2, 4]])

# Ellipsis(...) in indexing
# selects all dimensions which are not explicitly mentioned
cube = np.random.rand(4, 4, 4)
print(cube)
print(cube[..., 0]) # this selects [everything, everything, 0]
                    
# Use np.newaxis to add new dimensions
arr = np.array([1, 2, 3, 4])
arr[:, np.newaxis]
print(arr[:, np.newaxis])

# Modify array by slice
arr[1:3] = 99 # indices 1-2
print(arr)

# Stack arrays of the same shape along the axis you specify
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked = np.stack((a,b), axis=0)
    # axis=0: a and b become rows.
    # axis=1: a and b become columns.
    # axis=-1: same as axis 1 because it refers to the last dimension.
print(stacked)

# Resize
# Unlike reshape, resize will modify the data
# will truncate data, or fill extra spaces with 0
arr = np.array([1, 2, 3, 4, 5, 6])
arr.resize((3, 4))
print(arr)

# Split arrays into sub-arrays
arr = np.array([1, 2, 3, 4, 5, 6])
uneven = np.array_split(arr, 4) # will allow uneven divides
print(uneven)
even = np.split(arr, 3) # will raise an error if does not split evenly
print(even)

# vertical splitting with .vsplit()
# horizontal splitting with .hsplit()
# .dsplit() for 3D arrays along the third axis (axis=2)



# Broadcasting
# allows us to perform arithmetic operations on arrays of different shapes
# without reshaping them
# does so by adjusting the smaller array and replicating values necessarily
a = np.array([[1, 2, 3], [4, 5, 6]])
x = [10, 1, 10]
print(a + x)

a = np.array([12, 24, 35, 45, 60, 72])
b = np.array(["Adult", "Minor"])
res = np.where(a > 18, b[0], b[1])
print(res)