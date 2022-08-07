
class Pycharm:

    def execute(self):
        print("compiling")
        print("runnning")

class Myeditor:
    def execute(self):
        print("spell")
        print("convention")
        print("compiling")
        print("running")
class Laptop:

    def code(self,ide):
        ide.execute()

ide = Myeditor()

lap1 = Laptop()
lap1.code(ide)