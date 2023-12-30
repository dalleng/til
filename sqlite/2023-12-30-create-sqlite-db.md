# Create a sqlite database

SQLite comes with a cli tool called `sqlite3`, you can create a db by executing:

`sqlite3 test.db`

After executing, you will enter a command prompt in which you can enter SQL (terminated by ;). To terminate the sqlite3
program type your system End-Of-File character (usually a Control-D).

## Initialize a database with a SQL script

`sqlite3 test.db -init create_table.sql`

## Initialize a database without entering the command prompt

`sqlite3 test.db ".read create_table.sql"`

[Source](https://www.sqlite.org/cli.html)