
a = 10

def something():
    global a
    a = 15

    print("in fun ",a)

    a = 9

something()


print("out", a)
