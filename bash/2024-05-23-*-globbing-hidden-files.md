# `*` in shell globbing does not match hidden files

When executing something like `ls *.py` in the shell, hidden files (files starting with `.` in Unix-like operating systems)
will not be included. See:

```bash
$ ls -a
.  ..  .hidden.toml
$ ls *toml
ls: cannot access '*toml': No such file or directory
```

To find hidden files, this can be used:

`ls .*toml`

or if you want to include both hidden and non-hidden files:

`ls .*toml *toml`

