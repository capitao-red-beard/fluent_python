from array import array
import math


class Vector2d:
    # typecode is a class attribute we'll use when converting Vector2d 
    # instances to/from bytes.
    typecode = 'd'

    def __init__(self, x, y):
        # converting x, y into float in init catches errors early, 
        # useful if Vector2d is called with incorrect arguments.
        self.x = float(x)
        self.y = float(y)
    
    # __iter__ makes a Vector2d iterable; this is what makes unpacking 
    # work (e.g. x, y = my_vector). We implement it simply by using a 
    # generator expression to yield the components one after the other.
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    # __repr__ builds a string interpolating the components with {!r} 
    # to get their repr; because Vector2d is iterable, *self feeds the 
    # x and y components to format.
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r}'.format(class_name, *self)
    
    def __str__(self):
        # From an iterable Vector2d, it's easy to build a tuple for 
        # display as an ordered pair.
        return str(tuple(self))

    # To generate bytes, we convert the typecode to bytes and 
    # concatenate...
    def __bytes__(self):
        # ... bytes converted from an array built by iterating over the 
        # instance.
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))
    
    # To quickly compare all components, build tuples out of the 
    # operands. This works for operands which are instances of 
    # Vector2d, but has issues. 
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    # The magnitude is the length of the hypotenuse of the triangle 
    # formed by the x and y components.
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        # bool uses abs(self) to compute the magnitude, then converts 
        # it to bool, so 0.0 becomes False, nonzero is True.
        return bool(abs(self))

    # classmethod is decorated by the classmethod decorator.
    @classmethod
    # No self argument; instead, the class itself is passed as cls.
    def frombytes(cls, octets):
        # Read typecode from the first byte.
        typecode = chr(octets[0])
        # Create a memoryview from the octets binary sequence and use 
        # typecode to cast it.
        memv = memoryview(octets[1:]).cast(typecode)
        # Unpack the memoryview resulting from the cast into the pair 
        # of arguments needed for the constructor.
        return cls(*memv)
