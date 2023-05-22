# Debugging celery tasks

The `celery.contrib.rdb` package can be used to do remote debugging on celery tasks. It is an extension of PDB.

Sample usage:
```python
from celery import task
from celery.contrib import rdb

@task()
def add(x, y):
    result = x + y
    rdb.set_trace()  # <- set break-point
    return result
```

To attach to the process running the task and use the debugger, run the following on a terminal window:

```bash
$ telnet localhost 6900
```

[Source](https://docs.celeryq.dev/en/stable/userguide/debugging.html#basics)
