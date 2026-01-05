# The `cardinality` function in PostgreSQL

Returns the number of elements in the array or 0 if it's empty. If the column value is NULL, returns NULL.

See example:

```sql
create table users (
  id serial primary key,
  first_name varchar(50),
  last_name varchar(50),
  favorite_colors text[]
)

insert into users (first_name, last_name, favorite_colors)
values ('Bruce', 'Wayne', array ['black']),
        ('Peter', 'Parker', array ['red', 'blue']),
        ('John', 'Doe', null),
        ('Jane', 'Doe', array[]::text[]);
```

```sql
diegoallen@/tmp:diegoallen> select u.*, CARDINALITY(u.favorite_colors) as n_fav_colors from users u;
+----+------------+-----------+-----------------+--------------+
| id | first_name | last_name | favorite_colors | n_fav_colors |
|----+------------+-----------+-----------------+--------------|
| 1  | Bruce      | Wayne     | ['black']       | 1            |
| 2  | Peter      | Parker    | ['red', 'blue'] | 2            |
| 3  | John       | Doe       | <null>          | <null>       |
| 4  | Jane       | Doe       | []              | 0            |
+----+------------+-----------+-----------------+--------------+
```

Use coalesce to show `NULL` columns as `0`.

```sql
diegoallen@/tmp:diegoallen> select u.*, coalesce(CARDINALITY(u.favorite_colors), 0) as n_fav_colors from users u;
+----+------------+-----------+-----------------+--------------+
| id | first_name | last_name | favorite_colors | n_fav_colors |
|----+------------+-----------+-----------------+--------------|
| 1  | Bruce      | Wayne     | ['black']       | 1            |
| 2  | Peter      | Parker    | ['red', 'blue'] | 2            |
| 3  | John       | Doe       | <null>          | 0            |
| 4  | Jane       | Doe       | []              | 0            |
+----+------------+-----------+-----------------+--------------+
```
