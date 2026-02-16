# The `__file__` attribute in python

In Python modules and packages have the `__file__` attribute which is a string with the absolute path of the file with the module
or the `__init__.py` of the package. It could also be the `.so` file of a compiled extension module.

Examples:

```shell
In [1]: import collections

In [2]: collections.__file__
Out[2]: '/Users/diegoallen/.asdf/installs/python/3.11.1/lib/python3.11/collections/__init__.py'

In [3]: import inspect

In [4]: inspect.__file__
Out[4]: '/Users/diegoallen/.asdf/installs/python/3.11.1/lib/python3.11/inspect.py'

In [5]: import math

In [6]: math.__file__
Out[6]: '/Users/diegoallen/.asdf/installs/python/3.11.1/lib/python3.11/lib-dynload/math.cpython-311-darwin.so'
```

It can be very useful to quickly locate a virtualenv and check the code of either standard library modules or third party dependencies.