#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 

import math
import string
import os
from os import walk
#from os.path import isfile, join
from os import listdir
import random
import sys


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [x**2 for x in range(20)]
print(square)


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two= [2**i for i in range(50)]
print(power_of_two)


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt= [math.sqrt(num) for num in range(100)]
print(sqrt)


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

#One way

my_list = [num for num in range(-10,1)]

#Other way

results = [-num for num in reversed(range(11))]
print(my_list)
print(results)



#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds = [num for num in range(1,100) if num % 2 != 0]
print(odds)


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven= [num for num in range(1,1000) if num % 7 == 0]
print(divisible_by_seven)


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'

vowels = ['a','e','i','o','u',' ']
non_vowels = [letter for letter in teststring if letter.lower() not in vowels]
print(non_vowels)


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

teststring = 'The Quick Brown Fox Jumped Over The Lazy Dog'

#One way
capital_letters = [letter for letter in teststring if letter in string.ascii_uppercase]

#Other way
results = [letter for letter in teststring if letter.isupper()]

print(capital_letters)
print(results)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

teststring = 'The quick brown fox jumped over the lazy dog'
vowels = ['a','e','i','o','u',' ']
consonants = [letter for letter in teststring if letter.lower() not in vowels]
print(consonants)


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

mypath = '../madrid-oct-2018'
files = [folder for folder in next(os.walk(mypath))[1]]
print(files)


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_lists = [random.sample(range(101),10) for _ in range (4)]
print(random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list = [y for x in list_of_lists for y in x]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [[float(y) for y in x] for x in list_of_lists]
print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 

try:
    for i in ['a','b','c']:
        print (i**2)
except:
    print ("An error occurred!")


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:4
    print ("Can't divide by Zero!")
finally:
    print ('All Done!')


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]

#print(abc[3])
try:
    i = int(input("Enter item index to print: "))
except IndexError:
    print ("List index out of range!")
else:
    print(abc[i])


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

try:
    x = int( input( "enter a number: " ) )
    y = int( input( "enter another number: " ) )
    print( x, '/', y, '=', x/y )
except ZeroDivisionError:
    print( "Can't divide by 0!" )
except ValueError:
    print( "That doesn't look like a number!" )
except:
    print( "something unexpected happend!" )


#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('test','r')
    f.write('Test write this')
except IOError:
   print ("Error: File not found or is read-only")
else:
   print ("Content written successfully")
   f.close()


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except (IOError,ValueError) as e:
    print ("Please check the file,either the file is read-only or the data can't be converted to an integer.",e.errno)
except: 
    print ("Unexpected error")


#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')

# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

def ask():

    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print ("Looks like you did not enter an integer!")
            continue
        else:
            print ('Yep thats an integer!')
            break

    print ('Thank you, your number squared is: ', n**2)


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results = [number for number in range(1,1001) if True in [True for divisor in range(2,10) if number % divisor == 0]]
print(results)


# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)

Total_Marks = int(input("Enter Total Marks Scored: "))
try:
    Num_of_Sections = int(input("Enter Num of Sections: "))
    if(Num_of_Sections < 2):
        raise UnAcceptedValueError("Number of Sections can't be less than 2")
except UnAcceptedValueError as e:
    print ("Received error:", e.data)


