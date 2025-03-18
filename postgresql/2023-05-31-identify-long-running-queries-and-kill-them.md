# Identify long running queries and kill them.

The pg_stat_activity table provides real-time information on active database sessions, including running queries, duration, user, and application. It’s useful for monitoring and troubleshooting performance issues.

## Find Long-Running Queries

The following query identifies queries running for more than 5 minutes:

```sql
SELECT
  pid,
  now() - pg_stat_activity.query_start AS duration,
  query,
  state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';
```

## Cancel a query

To stop a query gracefully, use:

```sql
SELECT pg_cancel_backend(__pid__);
```
(It may take a few seconds to take effect.)

## Force Termination

If you want to force quit, the equivalent of a `kill -9`, you can use `pg_cancel_backend` instead. See:

```sql
SELECT pg_terminate_backend(__pid__);
```

## Kill All Existing Queries

To terminate all currently running queries (excluding the current session), run:

```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE pid <> pg_backend_pid();
```

Warning: This will forcefully terminate all active queries, which may cause disruptions.

[Source](https://medium.com/little-programming-joys/finding-and-killing-long-running-queries-on-postgres-7c4f0449e86d)