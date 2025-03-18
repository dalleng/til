# Useful queries to check existing connections

## List All Active Connections

```sql
SELECT
  pid,
  usename AS user,
  datname AS database,
  client_addr AS client,
  application_name,
  state,
  query,
  backend_start,
  state_change
FROM pg_stat_activity;
```

This query retrieves details on all active connections, including the user, database, client address, application, and query being executed.

## List Connections for a Specific Database

```sql
SELECT pid, usename, client_addr, state, query
FROM pg_stat_activity
WHERE datname = 'your_database_name';
```

## Count the Number of Active Connections

This query shows how many connections exist per database.

```sql
SELECT datname, count(*) AS connection_count
FROM pg_stat_activity
GROUP BY datname;
```

## List Idle Connections (Potentially Stale)

Idle connections are those that are open but not actively executing a query.

```sql
SELECT pid, usename, client_addr, state, query
FROM pg_stat_activity
WHERE state = 'idle';
```

## Identify Connections from a Specific User

```sql
SELECT pid, datname, client_addr, state, query
FROM pg_stat_activity
WHERE usename = 'your_username';
```