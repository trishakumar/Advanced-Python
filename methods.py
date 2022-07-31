class Student:

    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is student class in abc module")

s1 = Student(34,56,78)
s2 = Student(12,45,76)

print(s1.avg())
print(Student.info())

Student.info()
