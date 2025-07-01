# Dictionary view objects

The objects returned by `dict.keys()`, `dict.values()` and `dict.items()` are view objects.
They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.

`iter(dictview)` can be used to get an iterator. See the following example:

```
In [1]: d = {'foo': 'bar'}

In [2]: i = iter(d.values())

In [3]: next(i)
Out[3]: 'bar'

In [4]: next(i)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In [4], line 1
----> 1 next(i)

StopIteration: 
```


[Source](https://docs.python.org/3/library/stdtypes.html#dict-views)