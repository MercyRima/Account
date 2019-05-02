class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        radius = self.radius
        a = (22/7)*(radius*radius)
        print(a)
    def circumference(self):
        radius = self.radius
        a = 2*(22/7)*radius
        print(a)

class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        side = self.side
        n = side*side
        print(n)
    def perimeter(self):
        side = self.side
        n = 4*side
        print(n)

class Rectangle:
    def __init__(self,W,L):
        self.W = W
        self. L = L
    def area(self):
        W = self.W
        L = self.L
        h = W*L
        print(h)
    def perimeter(self):
        L = self.W
        L = self.L
        l = 2*(W+L)
        print(L)

class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def S_area(self):
        radius = self.radius
        m=4*(22/7)*radius*radius
        print(m)
    def volume(self):
        radius = self.radius
        v = (4/3)*(22/7)*radius*radius*radius
        print(v)

