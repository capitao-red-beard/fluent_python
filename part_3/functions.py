from functools import reduce, partial
from operator import add, mul
import random
from inspect import signature
import inspect
from operator import mul, itemgetter, attrgetter, methodcaller
from collections import namedtuple
import unicodedata
import functools


# Treating a function like an object.
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
# __doc__ is one of several attributes of function objects.
print(factorial.__doc__)
# factorial is an instance of the function class.
print(type(factorial))

fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))
print(list(map(fact, range(11))))

# Higher-order functions.
# A function which takes a function as an argument or returns a
# function.
fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
print(sorted(fruits, key=len))

# Sorting a list of words by their reverse spelling.
def reverse(word):
    return word[::-1]


print(reverse("testing"))
print(sorted(fruits, key=reverse))

# Modern replacements for map, filter and reduce.
# Build a list of factorials from 0! to 5!.
print(list(map(fact, range(6))))
# With list comp.
l = [fact(n) for n in range(6)]
print(l)
# List of factorials of odd numbers up to 5!.
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
# With list comp.
l2 = [factorial(n) for n in range(6) if n % 2]
print(l2)
# Sum integers up to 99, we imported add to avoid creating an add
# function ourselves.
print(reduce(add, range(100)))
# Same using sum, no import or adding needed.
print(sum(range(100)))

# Anonymous functions.
# Small, one-off functions.
# lambda keyword creates an anonymous function within a Python
# expression.
print(sorted(fruits, key=lambda word: word[::-1]))

# The seven falvours of callable objects.

# User-defined functrions: Created with def statements or lambda
# expressions.

# Built-in functions: A function implemented in C, like len.

# Built-in methods: Methods implemented in C, like dict.get.

# Methods: Functions defined in the body of a class.

# Classes: When invoked, a class runs its __new__ method to create an
# instance, then __init__ to initialise it, and finally the instance is
# returned to the caller. Because there is no new operator in Python,
# calling a class is like calling a function.

# Class instances: If a class defines a __call__ method, then its
# instances may be invoked as functions.

# Generator functions: Functions or methods that use the yield keyword.
# When called, generator functions return a generator object.

# Test if an object is callable.
print(callable(abs))
print(callable(str))
print(callable(13))


# User-defined callable types.
class BingoCage:

    # Accepts any literal; building a local copy prevents unexpected
    # effects on any list passed in.
    def __init__(self, items):
        self._items = list(items)
        # Shuffle garuanteed to work because _items is a list.
        random.shuffle(self._items)

    # The main method.
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            # Raise custom exception method if _items is empty.
            raise LookupError("Pick from empty BingoCage")

    # Shortcut to bingo.pick(): bingo().
    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))

# Function introspection.
print(dir(factorial))


def upper_case_name(obj):
    return f"{obj.first_name} {obj.last_name}".upper()


upper_case_name.short_description = "Customer name"

# Listing attributes of functions that don't exist in plain instances.
# Create bare user defined class.
class C:
    pass


# Make an instance of the class.
obj = C()

# Create a bare function.
def func():
    pass


# Using set differences, generate a sorted list of the attributes that
# exist in a function but not in an instance of a bare class.
print(sorted(set(dir(func)) - set(dir(obj))))

# From positional to keyword-only parameters.
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs["class"] = cls
    if attrs:
        attr_str = "".join(
            ' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items())
        )
    else:
        attr_str = ""
    if content:
        return "\n".join("<%s%s>%s</%s>" % (name, attr_str, c, name) for c in content)
    else:
        return "<%s%s />" % (name, attr_str)


# A single positional argument produces an empty tag with that name.
print(tag("br"))
# Any number of arguments after the first are captured by *content as a
# tuple.
print(tag("p", "hello"))
print(tag("p", "hello", "world"))
# Keyword arguments not explicitly named in then tag signature are
# captured by **attrs as a dict.
print(tag("p", "hello", id=33))
# The cls parameter can only be passed as a keyword argument.
print(tag("p", "hello", "world", cls="sidebar"))
# Even the first positional argument can be passed as a keyword when
# tag is called.
print(tag(content="testing", name="img"))
my_tag = {
    "name": "img",
    "title": "Sunset Boulevard",
    "src": "sunset.jpg",
    "cls": "framed",
}
# Prefixing the my_tag dict with ** passes all its items as separate
# arguments, which are then bound to the named parameters, with the
# remaning caught by **attrs.
print(tag(**my_tag))

# Retrieving information about parameters.
def clip(text: str, max_len: "int > 0" = 80) -> str:
    """ Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(" ", 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # No spaces were found.
        end = len(text)
    return text[:end].rstrip()


# Returns the default parameter values of a function.
print(clip.__defaults__)
# Returns where the code exists.
print(clip.__code__)
# Returns a tuple of variables used in the function.
print(clip.__code__.co_varnames)
# Returns the number of arguments a function has.
print(clip.__code__.co_argcount)

sig = signature(clip)
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ":", name, "=", param.default)

sig = inspect.signature(tag)
# Pass a dict of arguments to bind.
bound_args = sig.bind(**my_tag)
print(bound_args)
# Iterate over the items in bound_args.arguments, which is an
# OrderedDict, to display the names and values of the arguments.
for name, value in bound_args.arguments.items():
    print(name, "=", value)
# Remove the mandatory argument name from my_tag.
del my_tag["name"]
# Throws error complaining of missing parameter name.
# mbound_args = sig.bind(**my_tag)

# Function annotations.
print(clip.__annotations__)
print(sig.return_annotation)
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ":", param.name, "=", param.default)

# Packages for functional programming.
# The operator module.
def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


def fact(n):
    return reduce(mul, range(1, n + 1))


metro_data = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paolo", "BR", 19.649, (-23.547778, -46.635833)),
]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

# Use namedtuple to define LatLong.
LatLong = namedtuple("LatLong", "lat long")
# Use namedtuple to define Metropolis.
Metropolis = namedtuple("Metropolis", "name cc pop coord")
# Build metro_areas list with Metropolis instances; note the nested
# tuple unpacking to extract (lat, long) and use them to build the
# LatLong for the coord attribute of Metropolis.
metro_areas = [
    Metropolis(name, cc, pop, LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_data
]
print(metro_areas[0])
# Reach into element metro_areas[0] to get its latitude.
print(metro_areas[0].coord.lat)
# Define a attrgetter to retrieve the name and the coord. lat nested
# attribute.
name_lat = attrgetter("name", "coord.lat")

# Use attrgetter again to sort a list of cities by latitude.
for city in sorted(metro_areas, key=attrgetter("coord.lat")):
    # Use the attrgetter defined above to show only city name and lat.
    print(name_lat(city))

s = "The time has come"
upcase = methodcaller("upper")
print(upcase(s))
hiphenate = methodcaller("replace", " ", "-")
print(hiphenate(s))

# Freezing arguments with functools.partial.
# Create a new triple function from mul.
triple = partial(mul, 3)
# Test it.
print(triple(7))
# Use triple with map; mul would not work with map in this example.
print(list(map(triple, range(1, 10))))

nfc = functools.partial(unicodedata.normalize, "NFC")
s1 = "café"
s2 = "cafe\u0301"
print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))
