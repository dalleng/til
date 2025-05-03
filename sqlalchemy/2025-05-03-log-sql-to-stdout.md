# Log SQL to stdout

- Use the `echo=True` parameter when creating an engine with `create_engine`.

```python
>>> from sqlalchemy import create_engine
>>> engine = create_engine("sqlite://", echo=True)
```

- Set `.bind.echo` on a [`Session`](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#executing-with-an-orm-session) instance

```python
session.bind.echo = True
```