from functools import reduce
from operator import add
import random


# Treating a function like an object.
def factorial(n):
    '''returns n!'''
    return 1 if n <2 else n * factorial(n-1)

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
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

# Sorting a list of words by their reverse spelling.
def reverse(word):
    return word[::-1]

print(reverse('testing'))
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
            raise LookupError('Pick from empty BingoCage')
    
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
    return f'{obj.first_name} {obj.last_name}'.upper()

upper_case_name.short_description = 'Customer name'

# Listing attributes of functions that don't exist in plain instances.
# Create bare user defined class.
class C: pass


# Make an instance of the class.
obj = C()

# Create a bare function.
def func(): pass

# Using set differences, generate a sorted list of the attributes that 
# exist in a function but not in an instance of a bare class.
print(sorted(set(dir(func)) - set(dir(obj))))

# From positional to keyword-only parameters.
