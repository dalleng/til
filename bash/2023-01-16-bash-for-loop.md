# For loops in bash

With an interval

```bash
for i in {1..10};
do
    echo "line $i"
done
```

Loop through filenames:

```bash
for file in *.json; do
ls -l $file
done
```

Loop using the output of a subcommand:
```bash
for file in $(find . -name '*.json'); do
ls -l $file
done
```

Single liner:
`for i in {1..5}; do echo $i; done`