# The `end` optional kwarg of the `print` built-in function.

The `print` built-in function has an optional keyworkd argument `end`, with the default value
`\n`. If you don't want to end all printed lines with a new line, you could use this.

```python
In [23]: print('hello', end=''); print(' world')
hello world
```