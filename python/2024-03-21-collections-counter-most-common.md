# `collections.Counter`'s `most_common` method

The `Counter` data structure from the collections module in Python's stdlib, is a dictionary-like
object that lets you count elements in an iterable.

```python
In [1]: from collections import Counter

In [2]: c = Counter('AABCDEFF')

In [3]: c
Out[3]: Counter({'A': 2, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 2})
```

The `most_common` takes an integer `n` as a parameter and returns the `n` most common elements in the iterable.

```python
In [5]: c.most_common()
Out[5]: [('A', 2), ('F', 2), ('B', 1), ('C', 1), ('D', 1), ('E', 1)]
```