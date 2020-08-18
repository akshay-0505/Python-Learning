class Students:

    school = 'viit'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3 = m3
#instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def getm1(self):
        return self.m1

    def setm1(self,m1):
        self.m1 = m1
 #class method
    @classmethod
    def info(cls):
        print(cls.school)

#static method
    @staticmethod
    def getSchool():
        print("This is studets info class")



s1 = Students(90,91,99)

print(Students.info())

print(s1.avg())

Students.getSchool()