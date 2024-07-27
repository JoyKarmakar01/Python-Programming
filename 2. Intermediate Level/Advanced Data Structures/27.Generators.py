# Using a generator function to yield values
def generate_numbers():
    for i in range(3):
        yield i

for number in generate_numbers():
    print(number)
# Output: 0 1 2
