# What does `...` mean in python?

## What's `...` or `Ellipsis`?

`...` or `Ellipsis` is a built-in constant.

```python
In [1]: ... is Ellipsis
Out[1]: True

In [2]: 'Ellipsis' in dir(__builtins__)
Out[2]: True
```

## `...` as a placeholder

Probably the most common usage for `...` is as a placeholder for functions, similar to how `pass` is used.

```python
def does_nothing():
    pass

def does_nothing2():
    3 # random constant used as a placeholder

def does_nothing3():
    # Similar to the previous example, but instead of using
    # an integer constant as a placeholder we use `...`
    ...
```

It can also be used as a placeholder in other situations, like class definitions:

```python
class ToDo:
    ...
```

It is also used as a sentinel value in an argument list, similar to how `None` is used.

```python
def foo(param=None)
    if param is None:
        param = 8 # assigns some default value
    ...

def foo2(param=...):
    if param is ...:
        param = 8 # assigns some default value
```


## `...` in type hinting

`...` has also special meanings in type hinting:

- `tuple[<type>, ...]`: means a tuple of any size but with all elements of type `<type>`.
E.g: `tuple[int, ...]` would represent any tuple that only contains ints.
- `Callable[..., <type>]`: means a callable that takes any type and number of arguments, but returns an element of `<type>`.
E.g: `Callable[..., int]` would represent any callable that returns an int.

### References:
- [When Do You Use an Ellipsis in Python?](https://realpython.com/python-ellipsis/)
- [Python 3: Ellipsis in function parameters?](https://stackoverflow.com/questions/54405918/python-3-ellipsis-in-function-parameters)
