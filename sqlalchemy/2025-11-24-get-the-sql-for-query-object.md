# Get the corresponding SQL from a query object

# For SQLAlchemy 1.x (ORM query objects)

```
compiled = query.statement.compile(dialect=query.session.bind.dialect)
print(str(compiled))       # SQL with :param_1 etc.
print(compiled.params)     # The actual parameter values
```

## SQLAlchemy 2.x (select() style)

```
from sqlalchemy.sql import select

stmt = select(User).where(User.id == 5)

print(
    stmt.compile(
        compile_kwargs={"literal_binds": True},
        dialect=engine.dialect
    )
)
```

## Wrapper for both

```
def to_sql(query):
    if hasattr(query, "statement"):  # legacy ORM Query
        stmt = query.statement
        dialect = query.session.bind.dialect
    else:
        stmt = query
        dialect = query.bind.dialect

    return str(stmt.compile(
        dialect=dialect,
        compile_kwargs={"literal_binds": True}
    ))
```
