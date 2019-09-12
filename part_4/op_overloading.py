from array import array
import reprlib
import math
import functools
import operator
import itertools
# Import the numbers module for type checking.
import numbers
from fractions import Fraction


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)
    
    def __mul__(self, scalar):
        # If scalar is an instance of numbers.Real subclass, create new 
        # Vector with multiplied components values.
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            # Otherwise return not implemented, to let Python try 
            # __rmul__ on the scalar operand.
            return NotImplemented
    
    def __rmul__(self, scalar):
        return self * scalar

    def __eq__(self, other):
        if isinstance(other, Vector):        
            return (len(self) == len(other) and 
                    all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented
