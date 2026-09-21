# Drop a constraint

- Basic example

```sql
ALTER TABLE <table_name> DROP CONSTRAINT already_existing_constraint;
```

- To avoid an error if the constraint does not exist

```sql
ALTER TABLE <table_name> DROP CONSTRAINT IF EXISTS already_existing_constraint;
```