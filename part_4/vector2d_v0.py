from array import array
import math


class Vector2d:
    # typecode is a class attribute we'll use when converting Vector2d 
    # instances to/from bytes.
    typecode = 'd'

    def __init__(self, x, y):
        # converting x, y into float in init catches errors early, 
        # useful if Vector2d is called with incorrect arguments.
        # Use exactly two underscores to make an attribute private.
        self.__x = float(x)
        self.__y = float(y)
    
    # The @property decorator marks the getter method of a property.
    # The getter method is named after the public property it exposes.
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    # Hash method making our class hashable.
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
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

    def __format__(self, fmt_spec=''):
        # If format ends with 'p' use polar coordinates.
        if fmt_spec.endswith('p'):
            # Remove 'p' suffix from fmt_spec.
            fmt_spec = fmt_spec[:-1]
            # Build tuple of polar coordinates: (magnitude, angle).
            coords = (abs(self), self.angle())
            # Configure outer format with angle brackets.
            outer_fmt = '<{}, {}>'
        else:
            # Otherwise, use x, y components of self for rectangle 
            # coordinates.
            coords = self
            # Configure outer format with parentheses.
            outer_fmt = '({}, {})'
        # Use the format built-in to apply the fmt_spec to each vector 
        # component, building an iterable of formatted strings.
        # Generate iterable with components as formatted strings.
        components = (format(c, fmt_spec) for c in self)
        # Plug the formatted strings into the outer format.
        return outer_fmt.format(*components)
    
    def angle(self):
        return math.atan2(self.y, self.x)


v1 = Vector2d(3, 4)
print(format(v1))
print(format(Vector2d(1, 1), 'p'))
print(format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '0.5fp'))
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))
print(set([v1, v2]))
