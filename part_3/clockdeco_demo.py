import time


# Implementing a simple decorator
def clock(func):
    # Define inner function clocked to accept any number of positional 
    # arguments.
    def clocked(*args):
        t0 = time.perf_counter()
        # This line only works because the closure for clocked 
        # encompasses the func free variable.
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
    # Return the inner function to replace the decorated function.
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == 'main':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
