# `types.SimpleNamespace`

Useful type for quick prototyping, when you need a class for which you can
add and remove attributes. Replacement for something like `class NS: pass`

```python
In [1]: from types import SimpleNamespace

In [3]: obj = SimpleNamespace(a=9, b=10, c=11)

In [4]: obj.a
Out[4]: 9

In [5]: obj.b
Out[5]: 10

In [6]: obj.c
Out[6]: 11
```