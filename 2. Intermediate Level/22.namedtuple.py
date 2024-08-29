from collections import namedtuple

# Defining and using a namedtuple
Point = namedtuple('Point', 'x y')
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20
