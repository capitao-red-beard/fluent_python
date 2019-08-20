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
