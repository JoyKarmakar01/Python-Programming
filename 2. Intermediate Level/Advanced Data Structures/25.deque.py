from collections import deque

# Using deque for efficient appends and pops
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3, 4])
