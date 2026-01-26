# Check whether an attribute has been loaded

The `inspect` function from SQLAlchemy can be used to inspect ORM instances and determine whether a relationship
(or deferred attribute) has been loaded from the database.

This is commonly done to:
- avoid accidentally triggering lazy loads
- prevent N+1 queries
- ensure it’s safe to serialize ORM objects without hitting the database

Example:

```python
from sqlalchemy import create_engine, select, inspect
from sqlalchemy.orm import Session

engine = create_engine(
    "postgresql+psycopg://postgres:postgres@localhost:5432/postgres",
    echo=True,  # log SQL to stdout
)

with Session(engine) as session:
    user = session.scalars(select(User)).one()
    print(inspect(user).unloaded)  # attributes that have not been loaded

[Source](https://docs.sqlalchemy.org/en/21/orm/mapping_styles.html#inspection-of-mapped-instances)