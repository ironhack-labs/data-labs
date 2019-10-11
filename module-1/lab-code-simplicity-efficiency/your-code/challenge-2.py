"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random # build dependency at the start instead

# drop the default arguments, changed l argument to "length", much easier to differentiate
def RandomStringGenerator(length=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        import random
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:
            import random
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))


# =====MY REFACTOR========
import random, string

options = string.ascii_letters + string.digits
def generateBatchOfStrings(num_str, min_str, max_str):
    return [[random.choice(options) for number in range(random.choice(range(min_str, max_str + 1)))] for i in range(1, num_str + 1)]
a = int(input('Enter minimum string length: ')) # ask for minimum value, immediately convert to an integer
b = int(input('Enter maximum string length: ')) # ask for maximum value, immediately convert to an integer
n = int(input('How many random strings to generate? ')) # ask for how many strings you want returned, immediately convert to an integer

print(generateBatchOfStrings(n, a, b))
