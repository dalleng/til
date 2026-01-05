# How to insert array literals

```sql
diegoallen@/tmp:diegoallen> create table arr_example (arr text[]);
CREATE TABLE
Time: 0.006s
diegoallen@/tmp:diegoallen> insert into arr_example (arr) values
 (array ['foo']),
 (array ['foo', 'bar']),
 (array[]::text[]),
 (null);
INSERT 0 4
Time: 0.001s
diegoallen@/tmp:diegoallen> select * from arr_example;
+----------------+
| arr            |
|----------------|
| ['foo']        |
| ['foo', 'bar'] |
| []             |
| <null>         |
+----------------+
SELECT 4
Time: 0.003s
```
