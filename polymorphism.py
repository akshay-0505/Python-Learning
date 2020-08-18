# Duck typing
#if there is bird walking like a duck quaking like a duck the it is Duck

class Pycharm:

    def execute(self):
        print("Compiled")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell ckeck")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()

ide = Pycharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)



