# Identify long running queries and kill them.

The `pg_stat_activity` table in PostgreSQL contains information about the current activity of database sessions. 
It provides details about active connections, including the queries being executed, their duration, the application and user associated with 
each connection, and various other statistics related to the current database activity. 
The table is commonly used for monitoring and troubleshooting purposes, allowing administrators to gain insights into the 
behavior and performance of database sessions.

The following query helps you identify long running queries. This can be useful to find queries that might be negatively affecting
performance in order to manually stop them.

```sql
SELECT
  pid,
  now() - pg_stat_activity.query_start AS duration,
  query,
  state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';
```

If you want to stop from the results of the previous query, you can use the following statement using the pid from the previous results.

```sql
SELECT pg_cancel_backend(__pid__);
```

It may take a few seconds to stop the query entirely using the pg_cancel_backend command.

If you want to force quit, the equivalent of a `kill -9`, you can use `pg_cancel_backend` instead. See:

```sql
SELECT pg_terminate_backend(__pid__);
```

[Source](https://medium.com/little-programming-joys/finding-and-killing-long-running-queries-on-postgres-7c4f0449e86d)