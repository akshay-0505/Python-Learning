class Car:
    wheels = 4
    def __init__(self):
        self.mil=10
        self.comp="maruti"

c1 = Car()

c1.mil = 20
print(c1.mil)
print(c1.wheels)
Car.wheels = 2
print(c1.wheels)