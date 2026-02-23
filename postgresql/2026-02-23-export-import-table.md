# Import/Export a table

Using the `\copy` command in `psql`

## Export a table

`\copy table to '/some-path/table.csv' with (format csv, header)`

**with a query**

`\copy (select * from table) to '/some-path/table.csv' with (format csv, header)`

**using binary format**

`\copy (select * from table) to '/some-path/table.bin' with (format binary)`

**Import a table**

`\copy table from '/some-path/table.csv' with (format csv, header)`

