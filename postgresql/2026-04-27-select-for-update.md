# Select rows for update

`SELECT ... FOR UPDATE` creates a row-level lock on the returned rows until the transaction commits or rolls back. Other transactions
executing a `SELECT ... FOR UPDATE`, `UPDATE`, or `DELETE` on those rows wait for the lock. How long they wait depends on the
`lock_timeout` and `statement_timeout` settings. In the case of `SELECT ... FOR UPDATE`, the behavior can be customized using
`SKIP LOCKED` and `NOWAIT`.

`SKIP LOCKED`: Skips the locked rows as if they didn't match the criteria in the `WHERE` clause.
`NOWAIT`: Throws an error immediately if any of the rows are locked.