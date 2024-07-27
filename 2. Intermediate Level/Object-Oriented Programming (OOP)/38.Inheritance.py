"""
Inheritance
Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).

"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        super().start()
        print(f"{self.brand} {self.model} is starting.")

my_car = Car("Toyota", "Corolla")
my_car.start()
# Output:
# Vehicle is starting.
# Toyota Corolla is starting.
