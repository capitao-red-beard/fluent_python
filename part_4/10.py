from array import array
import reprlib
import math
import numbers
import operator
import functools


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        # Protected array holding the Vector components.
        self._components = array(self.typecode, components)

    def __iter__(self):
        # To allow iteration, we return an iterator over
        # self._components.
        return iter(self._components)

    def __repr__(self):
        # Use reprlib.reptr() to get a limitred0length representation
        # of self._components.
        components = reprlib.repr(self._components)
        # Remove the array('d') before plugging the string into a
        # Vector constructor call.
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # Build a bytes object directly from self._components.
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        # If len is diferent, not equal.
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            # As soon as 2 components are different return false.
            if a != b:
                return False
        # Otherwise return True.
        return True

    def __hash__(self):
        # Compute a generator expression to lazily compute the hash of
        # each component.
        hashes = (hash(x) for x in self._components)
        # Feed hashes to reduce with the xor function to compute the
        # aggregate hash value; the third argument, 0, is the
        # initializer.
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        # We can't use hypot anymore so we sum the square roots of the
        # components and compute the sqrt of that.
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # Get the instance of the class for later use.
        cls = type(self)
        # If the index argument is a slice...
        if isinstance(index, slice):
            # ...invoke the class to build another Vector instance from
            # a slice of the _components array.
            return cls(self._components[index])
        # If the index is an int or another kind of integer...
        elif isinstance(index, numbers.Integral):
            # ...just return the specific item from self._components.
            return self._components[index]
        else:
            # Otherwise raise an exception.
            msg = '{cls.__name__} indeces must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        # Get the Vector class for later use.
        cls = type(self)
        # If the name is one char it may be one of the shortcut_names.
        if len(name) == 1:
            # Find the position of 1-letter name; str.find would also
            # locate 'yz' and we don't want that, this is the reason
            # for the test.
            pos = cls.shortcut_names.find(name)
            # If the position is within range, return the array element.
            if 0 <= pos < len(self._components):
                return self._components[pos]
        # If either test failed, raise AttributeError with a standard
        # message text.
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        # Special handling for single char attr names.
        if len(name) == 1:
            # If name is one from xyzt, set specific error message.
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            # If name is lowercase, set error message about all
            # single-letter names.
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            # Otherwise set black error message.
            else:
                error = ''
            if error:
                # If non-blank error message, raise AttributeError.
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        # Default case: call __setattr__ on superclass for standard
        # behaviour.
        super().__setattr__(name, value)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
