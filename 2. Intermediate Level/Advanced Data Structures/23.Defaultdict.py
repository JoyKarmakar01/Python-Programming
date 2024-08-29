from collections import defaultdict

# Using defaultdict to handle missing keys
fruit_count = defaultdict(int)
fruit_count['apple'] += 1
fruit_count['banana'] += 2
print(fruit_count)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
