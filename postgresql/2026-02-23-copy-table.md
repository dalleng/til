# Copy a table in Postgres

```sql
CREATE TABLE copy_of_table (LIKE table INCLUDING DEFAULTS INCLUDING INDEXES)
```

**INCLUDING options**

```sql
INCLUDING DEFAULTS        -- default values
INCLUDING IDENTITY        -- identity columns
INCLUDING GENERATED       -- generated columns
INCLUDING CONSTRAINTS     -- CHECK and UNIQUE constraints (NOT foreign keys)
INCLUDING INDEXES         -- indexes
INCLUDING COMMENTS        -- column/table comments
INCLUDING STATISTICS      -- extended statistics
INCLUDING STORAGE         -- storage settings
INCLUDING ALL             -- all of the above
```


