# Select a random row

```sql
SELECT * FROM table ORDER BY random() limit 1;
```

The above can be very slow for large tables. For a more detailed analysis and alternatives see: [https://stackoverflow.com/questions/8674718/best-way-to-select-random-rows-postgresql](https://stackoverflow.com/questions/8674718/best-way-to-select-random-rows-postgresql)