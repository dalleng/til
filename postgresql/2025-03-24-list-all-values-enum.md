# List all values of a Postgres enum

`SELECT unnest(enum_range(NULL::some_enum));`