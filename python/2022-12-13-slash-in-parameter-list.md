# What does `/` represent in the argument list of a function

A `/` is used to represent that all of the previous arguments are positional only.

```python
In [1]: def test(pos1, pos2, /, keyword_or_positional=10):
   ...:     print(f"pos1={pos1}, pos2={pos2}, keyword_or_positional={keyword_or_positional}")
   ...:

In [2]: test(10, 11, 12)
pos1=10, pos2=11, keyword_or_positional=12

In [3]: test(10, 11, keyword_or_positional=12)
pos1=10, pos2=11, keyword_or_positional=12
```