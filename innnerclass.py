class Student:

    def __init__(self,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.brand, self.cpu, self.ram)

    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8

s1 = Student('Navin',2)
s2 = Student('Jenny',3)

s1.show()

lap1 = Student.laptop()
