#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. 
#Assign the array to variable "a"
#Challenge: there are at least three easy ways that use numpy to generate random arrays.
#How many ways can you find?


#First method

a = np.random.random((2,3,5))

#Second method

a=np.random.rand(2,3,5)

##Third Method

a=np.random.randint(0,100,(2,3,5))



#4. Print a.

print(a)



#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.ones((5,2,3))



#6. Print b.

print(b)



#7. Do a and b have the same size? How do you prove that in Python code?

if a.shape == b.shape:
    print("a and b have the same size: " + str(a.shape))
else:
    print("a and b have different sizes; a is %s and b is %s" %(a.shape,b.shape))



#8. Are you able to add a and b? Why or why not?

np.add(a,b)

#The method will not work with arrays of different shapes
#This is because mathematically two matrices of different sizes is not defined, it can't be done



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c=np.transpose(b, (1,2,0))



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d=np.add(a,c)

#it now works because the shape of the two arrays are equal an therefore the mathematical operation is doable



#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

# In mathematical terms, addign two matrices means adding the value of each position with the value on the same position of the second matrix.
# All values in d are one unit higher than units in a because all values in matrix c were ones.



#12. Multiply a and c. Assign the result to e.

e=np.multiply(a,c)
print(a.shape)
print(c.shape)
print(e)



#13. Does e equal to a? Why or why not?

list1=[]
list2=[]

for x in e:
    for y in x:
        for z in y:
            list1.append(z)
                   
for i in a:
    for j in i:
        for k in j:
            list2.append(k)

            
if list1==list2:
    print(True)
else:
    print(False)
    
# e is equal to a because the command multiply  in numpy is the multiplication of each index with the corresponding in index in the other matrix
# Eijk*1=Eijk



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=d.max()
d_min=d.min()
d_mean=d.mean()




#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f=np.empty(d.shape)
print(f.shape)
print(f)



"""
#16. Populate the values in f. 
For each value in d, if it's larger than d_min but smaller than d_mean, assign 25
to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

counter0=0
counter1=0
counter2=0

for i in d:
    for j in i:
        for k in j:
            if k > d_min and k<d_mean:
                value=25
                
            elif k > d_mean and k<d_max:
                value=75
                
            elif k==d_mean:
                value=50
                
            elif k==d_min:
                value=0
                
            elif k==d_max:
                value=100
            f[counter0][counter1][counter2]= value
            if counter2<4:
                counter2+=1
            else:
                counter2=0
            
        if counter1<2:
            counter1+=1
        else:
            counter1=0
    if counter0<1:
        counter0+=1
    else:
        counter0=0
            

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
print(d)
print(f)




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
f=f.astype(str)
counter0=0
counter1=0
counter2=0

for i in d:
    for j in i:
        for k in j:
            if k > d_min and k<d_mean:
                value='B'
                
            elif k > d_mean and k<d_max:
                value='D'
                
            elif k==d_mean:
                value='C'
                
            elif k==d_min:
                value='A'
                
            elif k==d_max:
                value='E'
            f[counter0][counter1][counter2]= value
            if counter2<4:
                counter2+=1
            else:
                counter2=0
            
        if counter1<2:
            counter1+=1
        else:
            counter1=0
    if counter0<1:
        counter0+=1
    else:
        counter0=0
            

print(f)
