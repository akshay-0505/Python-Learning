from  abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        print("Runninh Process")

class Laptop(Computer):
    def process(self):
        print("Process in Laptop")

class Whitebord(Computer):
    def process(self):
        print("Process in whiteboard")

class Programmer():
    def work(self,com):
        print("Work is running")
        com.process();

comp1 = Laptop()

comp2 = Whitebord()

comp3 = Programmer()

comp3.work(comp1)

comp3.work(comp2)
