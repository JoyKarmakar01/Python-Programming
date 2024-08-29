"""
Static Methods
Static methods do not modify object state or class state and are utility functions that have a logical connection with the class. They use @staticmethod decorator.

"""

class Car:
    @staticmethod
    def car_sound():
        print("Vroom!")

Car.car_sound()  # Output: Vroom!
