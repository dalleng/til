# `str.isnumeric` method to check if all characters are numeric

Returns `true` for all non-empty strings that only contain numeric characters.

```In [1]: 'a'.isnumeric()
Out[1]: False

In [2]: ''.isnumeric()
Out[2]: False

In [3]: '1'.isnumeric()
Out[3]: True

In [4]: '123'.isnumeric()
Out[4]: True
```