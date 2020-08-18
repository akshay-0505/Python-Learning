class Computer:
    def __init__(self,i):
        self.name=i
        print(i)
    def config(self):
        print("this is computer with 64 but porcessor",self.name)


c = Computer("akshay")
c.config()
print(c.name)
print(id(c))
print(memoryview)
