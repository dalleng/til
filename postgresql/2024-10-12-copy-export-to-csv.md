# Use COPY to export to CSV

In a psql shell, `\COPY (select * from table) to '/some/path/foo.csv' CSV HEADER;` can be used to export the result of a query to a CSV file.