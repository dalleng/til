# Pull and resolve conflicts by using changes from the origin.

Use:

```
git pull -X theirs <origin> <branchname>
```

or directly (if there's already a tracking branch associated to the local branch):

```
git pull -X theirs <origin> <branchname>
```

The `-X theirs` specify that the merge strategy in case of conflicts should be to use the changes from origin.

Also, if you want to avoid merge commits combine the former with `--rebase`. Like:

```
git pull -X theirs --rebase
```