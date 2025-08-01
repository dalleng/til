# `str.partition`

This method of `str` partitions a string into three parts if the separator passed as a parameter is found.
The 3-tuple returned as a result includes the text before the separator, the separator, and the text after the separator.

```python
>>> 'article:10309'.partition(':')
('article', ':', '10309')
```

If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

```python
>>> 'ab'.partition(',')
('ab', '', '')
```

[Source](https://docs.python.org/3/library/stdtypes.html#str.partition)