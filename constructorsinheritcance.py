class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature1 A working")

    def feature2(self):
        print("feature2 working")

class B:
    def __init__(self):
        print("in B init")


    def feature3(self):
        print("feature1 B working")

    def feature4(self):
        print("feature4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

        def feat(self):
            super().feature2()
a1 = C()
a1.feature1()