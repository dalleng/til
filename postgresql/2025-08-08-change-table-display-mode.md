# Change table display mode in `psql` and `pgcli`

In `psql`, the `\x` command toggles *expanded display mode*. When enabled, each row is displayed vertically rather than horizontally, which makes columns with long values easier to read.

In `pgcli`, `\x` works the same way, but there’s also a more versatile command: `\T <table_display_mode>`.  
This lets you choose from multiple output formats — for example:
- `vertical` (equivalent to `\x`)
- `html`
- `csv`
- `insert`
- `update`

These modes can make it easier to copy results into other tools or scripts.