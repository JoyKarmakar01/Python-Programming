"""
Instance Variables
These are attributes unique to each object. They are defined within methods and typically use self to access them.

"""



class Car:
    def __init__(self, make, model, year):
        self.make = make        # Instance variable
        self.model = model      # Instance variable
        self.year = year        # Instance variable

my_car = Car("Honda", "Civic", 2022)
print(my_car.make, my_car.model, my_car.year)  # Output: Honda Civic 2022


