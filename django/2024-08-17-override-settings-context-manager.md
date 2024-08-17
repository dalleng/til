# Use `override_settings` as a context manager

To override settings in tests django provides [`override_settings`](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#django.test.override_settings). In the docs it is only shown as a decorator, but the function can also be used as a context manager.

```python
    with override_settings(SOME_SETTING=true):
        ...
```