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
    return inner