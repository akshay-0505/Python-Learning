from modules import *

def hello():
    print(d)
    return 10,20,30
def main():
    d = "akshay"
    a, b, c = hello()
    print(a, b, c)

    print(add(a, b))

    print("Hello" + __name__)

if __name__ == "__main__":
    main()
