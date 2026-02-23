# The `__file__` Attribute in Python

In Python, modules and packages typically have a `__file__` attribute.
This attribute is a string containing the absolute path to the file from which the module was loaded.

- For a regular module, it points to the `.py` file.
- For a package, it points to the package’s `__init__.py`.
- For compiled extension modules, it may point to a shared object file (e.g., `.so`, `.pyd`).

## Examples

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

## Why It’s Useful

The `__file__` attribute is helpful when you need to:

- Quickly locate the active virtual environment.
- Inspect the source code of standard library modules.
- Review the implementation of third-party dependencies.