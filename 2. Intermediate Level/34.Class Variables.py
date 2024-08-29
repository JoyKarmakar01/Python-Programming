"""
Class Variables
These are shared across all instances of the class.

"""

class Car:
    wheels = 4  # Class variable

    def __init__(self, make, model):
        self.make = make  # Instance variable
        self.model = model  # Instance variable

car1 = Car("Honda", "Civic")
car2 = Car("Toyota", "Corolla")

print(car1.wheels, car2.wheels)  # Output: 4 4
Car.wheels = 3
print(car1.wheels, car2.wheels)  # Output: 3 3
