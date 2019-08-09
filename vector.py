from math import hypot

# create our vector class
class Vector:

    # initialise for a vector
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # returns string representation of an object for inspection
    # without this vector instances just show memory location
    # implement __repr__ because python defaults to this instead of __str__
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    # returns the absolute value of our vector object
    def __abs__(self):
        return hypot(self.x, self.y)

    # if __bool__ not created python tries __len__
    # if __len__ == 0 return false
    # return false if magnitude of vector is 0
    def __bool__(self):
        return bool(abs(self))

    # implements "+" operator for objects of this class
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    # implements "*" operator for objects of this class
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# instatiate our vector object(s)
v = Vector(5, 6)
v2 = Vector(4, 5)

# print a string representation of the vector obejct(s)
print(v)
print(v2)

# perform addition on our vector objects
print(v + v2)

# perform a bool check on our vector object
print(bool(v))

# print the absolute value of our vector
print(abs(v))
