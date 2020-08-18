from math import pow as m

def hello(a):
    for i in range(5):
        print("Hello"+a)
    return 1,2,3


a=float(input())
b=float(input())
c=a+b
print("Sum is",c)
p,q,r=hello("Akshay")
print(p,q,r)
print(eval(input("Enter expression")))