import random
import string

def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, l1=8, l2=12):
    r = []
    for a in range(n):
        r.append(RandomStringGenerator(random.choice(range(l1, l2))))
    return r

print(BatchStringGenerator(10))
