# `default` kwarg in `max` builtin

The `max` builtin function has an optional kwarg `default`, that lets you set a default
for the case of the provided iterable being empty.

```python
In [18]: max([], default=0)
Out[18]: 0
```