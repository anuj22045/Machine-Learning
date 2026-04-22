
# --------------------------------gate smashers----------------------

import numpy as np

# ------------------------Arrrays--------------------------------
# list1 = [10, 20, 30, 40, 50]
# array1  =np.array(list1, dtype = int)  #if convert into character then use dtype = str or 'U32'

# print(array1)
# type(array1)

# -------------------

# # 2dimensional array

# list1 = [[1,2,3], [4,5,6], [7,8,9]]  #row and column
# array2 = np.array(list1)
# print(array2)

# --------------------------


# # create array by using range 

# array1  = np.arange(1, 10) # it will create array from 1 to 9
# print(array1)

# array = np.arange(11, 17).reshape((2,3)) # it will create array from 11 to 16 and reshape it into 2 rows and 3 columns
# print(array)

# -----------------------------

#predefined arrays

# array1  =np.zeros((3,4)) # it will create an array of zeros with 3 rows and 4 columns
# print(array1)

# array2 = np.ones((2,5)) # it will create an array of ones with 2 rows and 5 columns
# print(array2)


# ---------------------------------# Attributes of Numpy---------------

 

# 5 types of attributes of numpy array
# ndim:- it return the dimension of the array (returns the total number of dimensions (axes) of a NumPy array)
# shape:- it return the rows and column of the array
# size:- it return the total number of elements in the array
# dtype:- it return the data type of the array elements
# itemsize:- it return the size of each element in bytes

# list1  = [10, 20, 30, 40, 50]
# array =  np.array(list1, dtype = int)
# print(array.ndim) 
 
# list1 = [[1,2,3], [4,5,6], [7,8,9]]
# array2 = np.array(list1)
# print(array2.shape) # it will return the number of rows and columns in the array

# list3 = [[1,2,3], [4,5,6], [7,8,9]]
# array3 = np.array(list3)
# print(array3.size) # it will return the total number of elements in the array

# list4 = [[1,2,3], [4,5,6], [7,8,9]]
# array4 = np.array(list4)
# print(array4.dtype) # it will return the data type of the array elements

# list5 = [[1,2,3], [4,5,6], [7,8,9]]
# array5 = np.array(list5)
# print(array5.itemsize) # it will return the size of each element in bytes


# -----------------------Indexing in numpy array --------------------

# access the data in the array by using idexing and slicing 

# array1 = np.array([10, 20,30, 40, 50])
# print(array1[0]) # it will return the first element of the array
# print(array1[-1]) # it will return the last element of the array
# print(array1[1:4]) # it will return the elements from index 1 to index 3 (4 is not included)
# print(array1[:3]) # it will return the first 3 elements of the array
# print(array1[2:]) # it will return the elements from index 2 to the end of the array

# array2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(array2[0,0]) # it will return the element at index (0,0) which is 1
# print(array2[1,2]) # it will return the element at index (1,2) which is 6
# print(array2[0:2, 1:3]) # it will return the elements
# # from index (0,1) to index (1,2) which is [[2,3], [5,6]]
# print(array2[:2, :2]) # it will return the first 2 rows and first 2 columns of the array which is [[1,2], [4,5]]
# print(array2[1:, 1:]) # it will return the elements from index (1,1) to the end of the array which is [[5,6], [8,9]]


# -----------------------Slicing in numpy array---------------------- 

# Slicing is used to access a range of elements in the array

# array1 = np.array([10, 20,30, 40, 50])
# print(array1[1:4]) # it will return the elements from index 1 to 3 (4 is not included)
# print(array1[:-1]) # it will return all elements except the last one
# print(array1[1:6:2]) # it will return the elements from index 1 to 5 with a step of 2  jump krega

# print(array1[-1:-3:-1]) # it will return the elements from index -1 to -3 in reverse order


# ------------------------Arithmetic operations on numpy array------------------------------------------  

# 1.addition 

# x = np.array([[1,2], [3,4]])
# y = np.array([[11,23], [13,14]])

# z = x+y
# print(z) # it will return the element wise addition of the two arrays which is [[12 25], [16 18]]

# z = x-y
# print(z) # it will return the element wise subtraction of the two arrays which is [[-10 -21], [-10 -10]]

# z = x @ y
# print(z) # it will return the matrix multiplication of the two arrays which is [[37 50], [73 122]]  

# z = y // x
# print(z) # it will return the element wise floor division of the two arrays which is [[11 11], [4 3]]



# ---------------------------Sorting in 2D array -----------------------

# import numpy as np
# 1. np.sort()- it will return the sorted array in ascending order in row wise by default
# 2. np.argsort() - it will return the indices of the sorted array in ascending order in row wise by default

# 3. np.array.sort() - it will sort the array in place in ascending order in row wise by default



# x = np.array([[12, 11, 15],
#               [21, 25, 20],
#               [18, 27, 16]])
# y = np.sort(x)
# print(y) # it will return the sorted array in ascending order in row wise  which is [[11 12 15], [20 21 25], [16 18 27]]

# y = np.sort(x, axis = 0) # it will return the sorted array in ascending order in column wise which is [[12 11 15], [18 25 16], [21 27 20]]
# print(y)

# #  argument concept it print the value of index 
# y = np.argsort(x, axis = 0) # it will return the indices of the sorted array in ascending order in row wise which is [[1 0 2], [0 2 1], [2 0 1]]
# print(y)  


# x = np.array([6,2,9,1,3,])
# y = np.sort(x)
# print(y) # it will return the sorted array in ascending order which is [1 2 3 6 9]

# y = np.sort(x) [::-1]
# print(y)

# y = np.argsort(x)
# print(y)


# Statistical operations in 1D array 
# 1. max
# 2. min
# 3. sum()
# 4. mean()
# 5. median()
# 6. std()
# 7. var()
# 8.prod()

x = np.array([10, 20, 30, 40, 50])
y = np.max(x)
print(y)

min = np.min(x)
print(min)

sum = np.sum(x)
print(sum)

median = np.median(x)
print(median)
 
mean = np.mean(x)
print(mean)

prod = np.prod(x)
print(prod)

var = np.var(x)
print(var)