# x = int("123")
# print(isinstance(x, int))

# x = set([1,2,2,2,3])
# print(isinstance(x, set)

#RECURSION CALLING ITSELF UNTIL IT MEET ITS INTERNAL REQUERIMENTS 

# def countto10(x):
#     if x < 10:
#         return countto10(x +1)
#     else:
#         return x 

# print(countto10(0))


# def inception(x):
#     if len(x) < 100:
#         return inception(x + "within a memory")
#     else:
#         return x + '.'

# print(inception("This is a memory"))


# def twodim(mat):
#     count=0
#     for item in mat:
#         if isinstance(item,list):
#             count+= twodim(item) 
#         return count+1  

# print(twodim([[1,2], [1,2,3],[1,2,3]]))


def addM(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        res.append(row)
    return res

print(addM([[1,2],[1,2]], [[1,2],[1,2]]))

class Student:
    # Initialize
    def __init__(self, name, adj):
      self.name = name
      self.adj = adj 
      
    # All other functions are class methods
    def nickname(self):
        return self.adj + ' ' + self.name

annie = Student("Annie", "Amazing")