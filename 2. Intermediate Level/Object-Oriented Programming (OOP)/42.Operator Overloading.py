""" 
Operator Overloading
Operator overloading allows you to define how operators work with your objects.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 2)
v3 = v1 + v2
print(v3)  # Output: Vector(3, 5)
