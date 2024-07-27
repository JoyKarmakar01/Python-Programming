""" 
Magic Methods and Operator Overloading
Magic methods (or dunder methods, for "double underscore") allow you to define behaviors for operators and built-in functions. They are named with double underscores before and after, like __init__, __str__, etc.

__init__ and __str__
"""
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car)  # Output: Toyota Corolla
