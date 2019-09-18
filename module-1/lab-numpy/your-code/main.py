#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.version.version)
"""
1.17.2
"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
# option 1
a = np.random.random((2,3,5))
# option 2
# a = np.random.randint(10, (2,3,5))
# option 3

#4. Print a.
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
# option 1
b = np.tile(1, (5,2,3))
# option 2
# b = np.ones((5,2,3))



#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
if a.size == b.size:
        print("They have the same size! They have an equal number of total elements housed within.")
else:
        print("The arrays are not the same size. They do not have have an equal number of total elements housed within.")



#8. Are you able to add a and b? Why or why not?
try:
        print(a + b)
except ValueError as err:
        print("No, they have different shapes, so we get the following error: " + str(err))



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable "c".
# c = b.transpose() # would return an array of 3x2x5, so we have to use the RESHAPE method to change it. Since they are all the same value, 1. just reshape
c = b.reshape(2, 3, 5)
print(c)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add(a, c)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("A is\n")
print(a)
print("D is\n")
print(d)
"""
Matrix d is exactly matrix a plus the value of one to each element.
"""

#12. Multiply a and c. Assign the result to e.
e = (a * c)

#13. Does e equal to a? Why or why not?
if np.array_equal(e, a):
        print("Yes, we have multiplied every element by 1, it retains its same value. This method array_equal will return true if shape and elements are identical")
else:
        print("Guess not?")

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = np.amax(d)
d_min = np.amin(d)
d_mean = np.mean(d)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2,3,5)) # something weird, it keeps populating f with the exact values as d?

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for x in range(len(d)):
        for y in range(len(d[x])):
                for z in range(len(d[x][y])):
                        if d[x][y][z] == d_max:
                                f[x][y][z] = 100
                        elif d[x][y][z] == d_mean:
                                f[x][y][z] = 50
                        elif d[x][y][z] == d_min:
                                f[x][y][z] = 0
                        elif d[x][y][z] < d_max and d[x][y][z] > d_mean:
                                f[x][y][z] = 75
                        else:
                                f[x][y][z] = 25

print("Matrix d is")
print(d)
print("The Max value is " + str(d_max))
print("The Mean value is " + str(d_mean))
print("The Min value is " + str(d_min))
print("Matrix f is")
print(f)
                        


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

g = d
h = np.ndarray.tolist((np.empty((2,3,5))))

for x in range(len(g)):
        for y in range(len(g[x])):
                for z in range(len(g[x][y])):
                        if g[x][y][z] == np.amax(g):
                                h[x][y][z] = 'E'
                        elif g[x][y][z] == np.mean(g):
                                h[x][y][z] = 'C'
                        elif g[x][y][z] == np.mean(g):
                                h[x][y][z] = 'A'
                        elif g[x][y][z] < np.amax(g) and g[x][y][z] > np.mean(g):
                                h[x][y][z] = 'D'
                        else:
                                h[x][y][z] = 'B'

print("Matrix g is")
print(g)
print("The Max value is " + str(np.amax(g)))
print("The Mean value is " + str(np.mean(g)))
print("The Min value is " + str(np.amin(g)))
print("Matrix h is")
# print(h)
print(np.char.array(h)) # to convert my nested list back into a string array
# all things considered though, how was I to complete this without using Numpy? 

