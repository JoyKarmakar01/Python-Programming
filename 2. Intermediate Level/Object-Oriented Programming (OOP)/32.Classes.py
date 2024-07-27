'''

Classes
A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects can have.

'''

class Car:
    # Attributes
    make = ""
    model = ""
    year = 0

    # Method (function defined inside a class)
    def start(self):
        print(f"The {self.make} {self.model} is starting.")

# Create an object (instance) of the Car class
my_car = Car()
my_car.make = "Toyota"
my_car.model = "Corolla"
my_car.year = 2021

# Access attributes and methods
print(my_car.make, my_car.model, my_car.year)  # Output: Toyota Corolla 2021
my_car.start()  # Output: The Toyota Corolla is starting.
