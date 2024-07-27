"""
Class Methods
These methods are bound to the class, not the instance. They can modify the class state that applies across all instances. They use @classmethod decorator and take cls as the first parameter.

"""

class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @classmethod
    def update_wheels(cls, count):
        cls.wheels = count

Car.update_wheels(6)
print(Car.wheels)  # Output: 6
