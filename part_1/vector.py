from math import hypot


# Create our vector class.
class Vector:

    # Initialise for a vector.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Returns string representation of an object for inspection.
    # Without this vector instances just show memory location.
    # Implement __repr__ because python defaults to instead of __str__.
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # Returns the absolute value of our vector object.
    def __abs__(self):
        return hypot(self.x, self.y)

    # If __bool__ not created python tries __len__.
    # If __len__ == 0 return false.
    # Return false if magnitude of vector is 0.
    def __bool__(self):
        return bool(abs(self))

    # Implements "+" operator for objects of this class.
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Implements "*" operator for objects of this class.
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# Instatiate our vector object(s).
v = Vector(5, 6)
v2 = Vector(4, 5)

# Print a string representation of the vector obejct(s).
print(v)
print(v2)

# Perform addition on our vector objects.
print(v + v2)

# Perform a bool check on our vector object.
print(bool(v))

# Print the absolute value of our vector.
print(abs(v))
