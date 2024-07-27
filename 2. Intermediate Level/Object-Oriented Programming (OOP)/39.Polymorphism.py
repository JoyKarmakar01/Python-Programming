
"""
Polymorphism
Polymorphism allows methods to do different things based on the object it is acting upon. In Python, this is often achieved through method overriding, where a child class provides a specific implementation of a method already defined in its parent class.

"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
# Output: 
# Woof!
# Meow!
