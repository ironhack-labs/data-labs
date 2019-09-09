# def list2string(lst):
#     string = ' '.join(lst)
#     return string

# to_string = ['John', 'was', 'a', 'man', 'of', 'many', 'talents']
# list2string(to_string)

# 'John was a man of many talents'

# def area_of_circle(r):
#     """Function that defines an area of a circle"""
#     a = r**2 * math.pi
#     return a

# print area_of_circle(1)


# def checkIfEven(x):
#     if x % 2 == 0 :
#         return True
#     else:
#         return False
# TERNERAY OPERATOR

# [return this] if [this is true] else [return that]

# print(checkIfEven(3))

# def anotherExample(arg1, arg2):
#     result = arg1 * arg2
#     if result > 4:
#         return True
#     return False

# print(anotherExample(3, 1))

def pickStudent(i):
    names = ['ed', 'an', 'elda']
    try:
        return names[i]
    except Exception as err:
        return err
print(pickStudent(3))p