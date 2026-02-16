# `inspect.get_file` function

The `inspect.get_file(object)` in Python returns the name of the file in which the object has been defined. Very useful to quickly
access and check the source code of standard library objects and functions and also third party dependencies. Example:

```shell
In [1]: from collections import deque

In [2]: inspect.getfile(deque)
Out[2]: '/Users/diegoallen/.asdf/installs/python/3.11.1/lib/python3.11/collections/__init__.py'
```

[Source](https://docs.python.org/3/library/inspect.html#inspect.getfile)