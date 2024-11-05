from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Testing the subclasses
circle = Circle(5)
square = Square(4)

print(f"Area of Circle: {circle.area():.2f}")  # Output: Area of Circle: 78.54
print(f"Area of Square: {square.area()}")      # Output: Area of Square: 16
