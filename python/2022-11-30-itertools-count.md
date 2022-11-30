# `itertools.count` to create an iterator that returns an infinite sequence of numbers

```python
In [2]: import itertools

In [3]: c = itertools.count()

In [4]: next(c)
Out[4]: 0

In [5]: next(c)
Out[5]: 1

In [6]: next(c)
Out[6]: 2
```

## Useful to create test data with a dynamic portion

```python
In [9]: test_email_generator = (f'diego{n}@example.com' for n in itertools.count())

In [10]: next(test_email_generator)
Out[10]: 'diego0@example.com'

In [11]: next(test_email_generator)
Out[11]: 'diego1@example.com'

In [12]: next(test_email_generator)
Out[12]: 'diego2@example.com'
```