import array as a
from locale import format

arr = a.array('i',[])
n = int(input("Enter the length of srray :"))
for i in range(n):
    x=int(input("Enter next value"))
    arr.append(x)
print(arr)
print(arr.buffer_info())
print("division is : {:>3.2f}".format(arr[0]/arr[2]))
arr2= a. array('i',[])
arr2=arr
print(arr2);