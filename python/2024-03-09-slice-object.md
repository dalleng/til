# `slice` built-in object

A `slice` object represents the set of indices specified by `range(start, stop, step)`. The `start` and `step` are optional.

Example:

```python
>>> s = slice(2)
>>> l = [1, 2, 3, 4, 5]
>>> l[s]
[1, 2]
>>> s = slice(1, 4)
>>> l[s]
[2, 3, 4]
```

Can be useful when creating a custom data structure that customizes indexing. Example:

```python
>> class CustomMap:
      def __getitem__(self, slice):
          start = slice.start
          stop = slice.stop
          step = slice.step
          print(f"{start=} {stop=} {step=}")
          # custom logic ...
>>> cm = CustomMap()
>>> cm[1:2:3]
start=1 stop=2 step=3
```