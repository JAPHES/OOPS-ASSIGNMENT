class Rectangle:
    def __init__(self, length, width=None):
        # if width is not provided, assume it's a square
        if width is None:
             self.length = length
             self.width = length
        else:
            self.length = length
            self.width = width

    def calculate_area(self):
        return self.length * self.width

# Testing the Rectangle class

# Creating a square (one argument)
square = Rectangle(5)
print (f"Square area: {square.calculate_area()}")

rectangle = Rectangle(5,10)
print(f"Rectangle area: {rectangle.calculate_area()}")