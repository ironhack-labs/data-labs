#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))

#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size)
print(b.size)

if a.size == b.size:
        print("Both Array have the same size of ", a.size)
else:
        print("A and B have diffetent sizes, A is ", a.size, "and B is ", b.size)

#8. Are you able to add a and b? Why or why not?

# np.add(a, b) - No because they have different sturctures

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.reshape(b,(2,3,5))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print("a = to", a)
print("d = to", d) #It worked because both have the same shape


#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)
print("e = to", e)

#13. Does e equal to a? Why or why not?

if np.array_equal(a,e):
        print("Yes they are")
else:
        print("No they are different")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print(d_max)
print(d_min)
print(d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5),dtype=float)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

# r1 = -1
# r2 = -1
# r3 = -1
# for z in d:
#         r1 +=1
#         for y in z:
#                 r2+=1
#                 for x in y:
#                         r3+=1
#                         print(x)
#                         if x > d_min and x < d_mean:
#                                 f[r3][r2][r1] = 25
#                         elif x > d_mean and x < d_max:
#                                 f[r3][r2][r1] = 75
#                         elif x == d_min:
#                                 f[r3][r2][r1] = 0
#                         elif x == d_max:
#                                 f[r3][r2][r1] = 100
# print(d)
# print(f)

for i in range(len(d)):
        for y in range(len(d[i])):
                for z in range(len(d[i][y])):
                        if d[i][y][z] > d_min and d[i][y][z] < d_mean:
                                f[i][y][z] = 25
                        elif d[i][y][z] > d_mean and d[i][y][z] < d_max:
                                f[i][y][z] = 75
                        elif d[i][y][z] == d_min:
                                f[i][y][z] = 0
                        elif d[i][y][z] == d_max:
                                f[i][y][z] = 100
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
print(f)
print(d)

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

bq = np.empty((2,3,5),dtype=float)

bq = bq.tolist()

for i in range(len(d)):
        for y in range(len(d[i])):
                for z in range(len(d[i][y])):
                        if d[i][y][z] > d_min and d[i][y][z] < d_mean:
                                bq[i][y][z] = "B"
                        elif d[i][y][z] > d_mean and d[i][y][z] < d_max:
                                bq[i][y][z] = "C"
                        elif d[i][y][z] == d_min:
                                bq[i][y][z] = "A"
                        elif d[i][y][z] == d_max:
                                bq[i][y][z] = "D"

bq = np.array(bq)
print(bq)
