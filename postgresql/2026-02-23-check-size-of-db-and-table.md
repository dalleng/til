# Check the size of a database or table

## Check the size of a database

`select pg_size_pretty(pg_database_size('db_name'))`

## Check the size of a table

### Total size (Data + Indices + TOAST)

`SELECT pg_size_pretty(pg_total_relation_size('public.your_table'));`

TOAST is Postgres’s mechanism for automatically compressing and offloading oversized column values into a hidden side table so rows can still fit within the 8KB page limit. It’s used when a row contains large values—typically in columns like TEXT, JSONB, BYTEA, large VARCHAR, or arrays.

### Show sizes separately

```sql
SELECT
  pg_size_pretty(pg_relation_size('public.your_table')) AS table_size,
  pg_size_pretty(pg_indexes_size('public.your_table')) AS indexes_size,
  pg_size_pretty(pg_total_relation_size('public.your_table')) AS total_size;
```