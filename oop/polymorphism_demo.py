import math

# Base Class
class Shape:
    def area(self):
        # This ensures that subclasses must implement their own version of area()
        raise NotImplementedError("Subclasses must implement the area() method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
