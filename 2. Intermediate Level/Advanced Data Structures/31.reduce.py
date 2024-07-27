from functools import reduce

# Using reduce to calculate the product of a list of numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
