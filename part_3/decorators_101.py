# Function decorators and closures.
def deco(func):
    def inner():
        print('running inner()')
        # deco returns its inner function object.
    return inner

@deco
# target is decorated by deco
def target():
    print('running target()')

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
    print(f'running register {func}')
    # Include func in registry.
    registry.append(func)
    # return func, we must return a function; here we return the same 
    # received as argument.
    return func

# f1 and f2 are decorated by register.
@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

# f3 is not decorated.
def f3():
    print('running f3()')

# main displays the registry, then calls f1(), f2() and f3().
def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

# main() is only invoked if registration runs as a script.
if __name__ == '__main__':
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
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units."""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items."""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

# No changes needed to best_promos, because it relies on promo_list.
def best_promo(order):
    """Select the best available discount."""
    return max(promo(order) for promo in promos)

# Variable scope in Python.
