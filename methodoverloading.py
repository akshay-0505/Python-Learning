#overloading is not allowed in python

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a =None, b = None ,c = None):
        if a and b and c :
            return a+b+c
        else:
            return None


s = Student(90,91)

print(s.sum(1,2,3))
print(s.sum(1,2))