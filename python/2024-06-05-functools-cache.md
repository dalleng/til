# Using `functools.cache` to memoize functions

The `functools.cache` decorator is an unbounded cache for functions, whenever a function is called
the cache is checked first to see if the return value is stored there before executing the function.
All parameters of the function need to be hashable since the cache uses a dictionary.

[Source](https://docs.python.org/3/library/functools.html#functools.cache)