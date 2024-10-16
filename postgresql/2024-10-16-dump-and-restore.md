# Dump and restore PostgreSQL databases

## Dump the database

`pg_dump --host=localhost --port=15432 --username=postgres <db_name> > test.dump`

## Restore the database

`psql <db_name> < test.dump`

You can also use `--username`, `--host`, `--port`, etc. with `psql`.