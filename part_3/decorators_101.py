import time
import html
from functools import singledispatch
from collections import abc
import numbers


# Function decorators and closures.
def deco(func):
    def inner():
        print("running inner()")
        # deco returns its inner function object.

    return inner


@deco
# target is decorated by deco
def target():
    print("running target()")


# Invoking the decorated target runs inner.
target()
# Inspection reveals that target is now a reference to inner.
print(target)

# When Python executes decorators.
# registry will hold reference to functions decorated by @register.
registry = []

# register takes function as argument.
def register(func):
    # Display which function is being decorated.
    print(f"running register {func}")
    # Include func in registry.
    registry.append(func)
    # return func, we must return a function; here we return the same
    # received as argument.
    return func


# f1 and f2 are decorated by register.
@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


# f3 is not decorated.
def f3():
    print("running f3()")


# main displays the registry, then calls f1(), f2() and f3().
def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()


# main() is only invoked if registration runs as a script.
if __name__ == "__main__":
    main()

# Decorator-enhanced strategy pattern.
# promos starts empty.
promos = []

# promotion decorator returns promo_func unchanged, after adding it to
# the promos list.
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


# Any function decorated by @promotion will be added to promos.
@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points."""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units."""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total * 0.1
    return discount


@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items."""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


# No changes needed to best_promos, because it relies on promo_list.
def best_promo(order):
    """Select the best available discount."""
    return max(promo(order) for promo in promos)


# Variable scope in Python.
b = 6


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


f3(3)
print(b)


# Closures.
class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

# The nonlocal declaration.
def make_averager_2():
    count = 0
    total = 0

    def averager_2(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager_2


# Generic functions with single dispatch.
def htmlize(obj):
    content = html.escape(repr(obj))
    return f"<pre>{content}</pre>"


print(htmlize({1, 2, 3}))
print(htmlize(abs))
print(htmlize("Heimlich & Co. \n- a game"))
print(htmlize(42))
print(htmlize(["alpha", 66, {3, 2, 1}]))

# singleddispatch marks the base function which handles the object type.
@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f"<pre>{content}</pre>"


# Each base function is decorated with @<<base_function>>.register
# (<<type>>).
@htmlize.register(str)
def _(text):
    content = html.escape(text).replace("\n", "<br>\n")
    return "<p>{0}</p>".format(content)


# The name of the specialised functions is irrelevant; _ is a good
# choice to make this clear.
# For each new type to receive special treatment, register a new
# function. numbers.Inegral is a virtual superclass of int.
@htmlize.register(numbers.Integral)
def _(n):
    return "<pre>{0} (0x{0:x})</pre>".format(n)


# You can stack several register decorators to support different types
# with the same function.
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"


# Stacked decorators.
"""
@d1
@d2
def f():
    print('f')
"""
# Is the same as.
"""
def f():
    print('f')

f = d1(d2(f))
"""

# A parameterized registration decorator.
# registry is now a set so adding or removing is faster.
registry = set()

# register takes an optional keyword argument.
# This is our decorator factory.
def register(active=True):
    # decorate is the actual decorator; takes function as argument.
    def decorate(func):
        print("running register(active=%s)->decorate(%s)" % (active, func))
        # Register func only if the active argument is True.
        if active:
            # If not active and func in registry, remove it.
            registry.add(func)
        else:
            registry.discard(func)
        # Because decorate is a decorator it must return a function.
        return func

    return decorate


# Must be invoked as a function, with the desired parameters.
@register(active=False)
def f1():
    print("running f1()")


@register()
def f2():
    print("running f2()")


def f3():
    print("running f3()")


# The main point is, that register() returns decorate, which is then
# applied to the decorated function.
