class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overload the + operator to add two vectors
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        # For easy printing of Vector objects
        return f"Vector({self.x}, {self.y})"

# Testing vector addition
v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2  # Using the overloaded + operator
print(v3)     # Output: Vector(4, 6)
