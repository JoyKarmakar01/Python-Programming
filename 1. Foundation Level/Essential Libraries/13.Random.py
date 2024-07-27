import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_integer}")

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

# Choose a random element from a list
my_list = ['apple', 'banana', 'cherry']
random_choice = random.choice(my_list)
print(f"Random choice from list: {random_choice}")
