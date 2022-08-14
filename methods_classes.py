class Rectangle:
    def __init__(self, c, l, w):
        self.color = c
        self.length = l
        self.width = w 
        
    def area(self):
        self.area = self.length * self.width
        return self.area 

    def perimeter(self):
        self.perimeter = (2*self.length) + (2*self.width)
        return self.perimeter

    def diagonal(self):
        self.diagonal = ((self.width)**2 + (self.width)**2) ** (1/2)
        return self.diagonal

    def volume(self, h):
        self.height = h
        self.volume = self.length * self.width * self.height
        return self.volume


myRect1 = Rectangle('red', 2, 1)
myRect2 = Rectangle('blue',4,2)
print('myRect1 length = ',myRect1.length)
print(myRect1.color)
print('myRect2 length = ',myRect2.length)
print(myRect2.color)
print('myRect1area = ', myRect1.area())
print('myRect2area = ', myRect2.area())
print('myRect1 diagonal = ', myRect1.diagonal())
myVol = myRect1.volume(5)
print('myRect1 volume = ', myVol)


