# `datetime.replace`

The `datetime.replace` function lets you replace any component of a datetime instance. For example, see the snippet
below creating a `datetime` instance of the current date but at the beginning of the day.

```python
In [1]: from datetime import datetime, timezone

In [2]: datetime.now(tz=timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
Out[2]: datetime.datetime(2025, 5, 3, 0, 0, tzinfo=datetime.timezone.utc)
```