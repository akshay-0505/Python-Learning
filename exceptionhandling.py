import modules
a = 5
b = 3
try:
    print("Resource opened")
    print(modules.add(a,b))
    print(a/b)
    a = int(input("Enter a nummber"))

    print(a)

except ZeroDivisionError as e1:
    print("Cannot divide number by 0",e1)

except ValueError as e1:
    print("Invalid Input",e1)

except Exception as e1:
    print("Something Went Wrong")

finally:
    print("Resource closed")


