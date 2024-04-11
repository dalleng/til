# `operator.attrgetter`

`attrgetter` returns a callable that fetches the attribute given as parameter. It can fetch one or more
attributes, and can also follow relations within objects. See example:

```python
In [1]: class Job:
   ...:     def __init__(self, role, company_name):
   ...:         self.role = role
   ...:         self.company_name = company_name
   ...: 

In [2]: class Person:
   ...:     def __init__(self, first_name, last_name, job):
   ...:         self.first_name = first_name
   ...:         self.last_name = last_name
   ...:         self.job = job
   ...: 

In [3]: j = Job('Software Engineer', 'Foo Inc.')

In [4]: p = Person('John', 'Doe', j)

In [5]: from operator import attrgetter

In [6]: attrgetter('first_name')(p)
Out[6]: 'John'

In [7]: attrgetter('first_name', 'last_name')(p)
Out[7]: ('John', 'Doe')

In [8]: attrgetter('job.company_name')(p)
Out[8]: 'Foo Inc.'
```

 It can be used to build a nested version of (getattr)[https://docs.python.org/3/library/functions.html#getattr].

```python
from operator import attrgetter


def getnestedattr(obj, path, default=None):
    try:
        return attrgetter(path)(obj)
    except AttributeError:
        return default
```