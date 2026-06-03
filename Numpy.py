#Numpy 
import numpy as np
print(np.__version__)

my_list = [1, 2, 3, 4]

array = np.array([1, 2, 3, 4 ]) #creates 1 dim array

array = array * 2 # multiplies everything in the array by 2

print(array)

print(type(array))

array = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
                  [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
                  [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", "-"]]])
#3 dim array, think of 3x3 matrices stacked 

print(array.ndim)
print(array.shape)

print(array[0,0,0])
"""multidimensional indexing = array[a,b,c] 
a = layer/row
b = column
c = item from left to right
"""

word = array[0,0,0] + array[2,0,0] + array [2,0,0]
print (word)

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array[start:end:step]

print(array[0::2])
print(array[::-2])

#accessing columns

print(array[:,0:3]) #first 3 columns of every row
print(array[:, 1::2]) #every other column of every row starting at column 1
print(array[0:2,0:2])

#scalar arithmetic 
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1/array2)
print(array1 ** array2)

#Vectorized math functions

array = np.array([1.0, 2, 3])
print(np.sqrt(array))

radii = np.array([1, 2, 3])
print(np.pi * radii ** 2) #area of a circle

#comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100) #returns boolean array
print(scores >= 60)
scores[scores < 60] = 0 #makes it so that any scores below 60 equal to 0 

"""
Broadcasting allows numpy to perform operations on arrays 
with different shapes by virtually expanding dimensions 
so they match the larger array's shape

The dimensions have the same size OR one of the dimensions has a size of 1
"""

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])
#compatible
print(array1.shape)
print(array2.shape)

print(array1 * array2)

array1 = np.array([[1, 2, 3, 4], 
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
array2 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
#not compatible

array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)
#compatible
print(array1 * array2)

#aggregate functions
#summarize data and typically return a single value
array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))

print(np.sum(array, axis = 1)) #sums all the rows

#Filtering

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18] #flattens 2d array, creates a new array
adults = ages[(ages >= 18) & (ages < 65)] # use & instead of and
seniors = ages[(ages >= 65)]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)

#preserving origin array without creating new array
adults = np.where(ages >= 1, ages, 0)
print(adults)

#random numbers 
rng = np.random.default_rng(seed = 1)
print(rng.integers(low = 1,high = 101, size = (3,2))) 
# range = 1-6, size gives number of randome numbers, (3,2) is two dimensional
#setting seed gives same result

#floating point number has the decimal portion
np.random.seed(seed = 1) # assigns a seed number

print(np.random.uniform()) #random number between 0 and 1
print(np.random.uniform(low = 1, high = 1, size = (3, 3)))

array = np.array([1, 2, 3, 4, 5])

rng = np.random.default_rng() 

print(array)
rng.shuffle(array) #shuffles values of the array
print(array)

rng = np.random.default_rng()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruit = rng.choice(fruits, size = (3, 3))
print(fruit)

