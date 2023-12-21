## `typing.NamedTuple`

In the [typing](https://docs.python.org/3/library/typing.html) module there's a typed
version of `collections.namedtuple`.

```python
class Employee(typing.NamedTuple):
    name: str
    age: int
    department: str
```

[source](https://docs.python.org/3/library/typing.html#typing.NamedTuple)