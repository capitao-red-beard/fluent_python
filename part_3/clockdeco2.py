import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f"{k}={w}" for k, w in sorted(kwargs.items())]
            arg_lst.append(", ".join(pairs))
        arg_str = ", ".join(arg_lst)
        print(f"[%{elapsed}0.8fs] {name}{(arg_str)} -> {result}")
        return result

    return clocked
