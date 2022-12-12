# `dict.setdefault`

`setdefault(self, key, default=None, /)`

The method inserts a new value for `key` in the dictionary if the key does not exist in the dictionary, if it already
exists in the dictionary it returns the value for it.

```python
>>> d1 = {}
>>> d2 = {'foo': 'bar'}
>>> d1.setdefault('foo', 'jazz')
'jazz'
>>> d1
{'foo': 'jazz'}
>>> d2.setdefault('foo', 'jazz')
'bar'
>>> d2
{'foo': 'bar'}
```