"""
memoize a given function. used as decorator.
see day 10 part 2 for usage example
"""
def memoize(func):
    memoized = {}
    def inner(i, *args):
        if i not in memoized:
            memoized[i] = func(i, *args)
        return memoized[i]
    def reset():
        nonlocal memoized
        memoized = {}
    inner.reset = reset
    return inner


"""
memoize any function in existence
experimental. performance impact unknown.
"""
def memoize_the_world(func):
    memoized = {}
    def inner(*args):
        key = tuple(args)
        if key not in memoized:
            memoized[key] = func(*args)
        return memoized[key]
    def reset():
        nonlocal memoized
        memoized = {}
    inner.reset = reset
    return inner


"""
increase the recursion depth quickly
"""
def increase_recursion(depth):
    from sys import setrecursionlimit
    setrecursionlimit(depth)


"""
profile a function
"""
def profile(func):
    import timeit
    count = 1000
    def inner(*args):
        result = None
        def timing():
            nonlocal result
            result = func(*args)

        print("profiled to take: " +
            str(round((timeit.timeit(timing, number=count) / count), 5))
            + "s")

        return result
    return inner