
from functools import  reduce

nums = [1,2,3,4,5,6,7,8,9]

f= lambda n : n%2==0

evens = list(filter(f,nums))

doubles = list(map(lambda n : n+2 ,evens))

sum = reduce(lambda a,b:a+b,doubles)
print(evens)
print(doubles)
print(sum)