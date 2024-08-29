"""
Encapsulation
Encapsulation restricts direct access to some of the object's components and can prevent the accidental modification of data. This is done using private or protected attributes/methods.  

"""

class Car:
    def __init__(self, make, model):
        self._make = make    # Protected attribute
        self.__model = model # Private attribute

    def get_model(self):
        return self.__model

    def set_model(self, model):
        if model != "":
            self.__model = model

my_car = Car("Ford", "Mustang")
print(my_car.get_model())  # Output: Mustang
# print(my_car.__model)    # This will raise an AttributeError
my_car.set_model("Fiesta")
print(my_car.get_model())  # Output: Fiesta
