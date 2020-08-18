class A:

    def __init__(self , name):
         self.name = name
         print(self.name)

    def features1(self):
        print("Feature 1 is working")

    def features2(self):
        print("Feature 2 is working")




# single level inheritance
class B(A):

    def __init__(self , addr , name):
        super(B,self).__init__(name)

        self.addr = addr
        print(self.addr)

    def features3(self):
        print("feature 3 is working")

    def features4(self):
        print("Feature 4 is working")



# multilveel inheritance

class C(B):




    def feature5(self):
        print("Feature 5 is working")

#multiple inheritance




a1 = A("Akshay")
a1.features1()
a1.features1()

b1 = B("Pune","Bhavesh")
b1.features1()
b1.features2()
b1.features3()
b1.features4()

#c1 = C()

#c1.features4()
#c1.features1()
#c1.feature5()

