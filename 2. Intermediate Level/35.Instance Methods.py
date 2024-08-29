"""
Instance Methods
These methods operate on an instance of the class and have access to the instance (via self) and class variables.

"""

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car make: {self.make}, Model: {self.model}")

my_car = Car("Ford", "Mustang")
my_car.display_info()  # Output: Car make: Ford, Model: Mustang
