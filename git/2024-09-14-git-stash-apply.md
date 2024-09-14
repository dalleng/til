# Applying a stash without removing it from the list

The stash list could be used to store small changes that are frequently applied, but for some reason you do not want
to commit.

`git stash list` can be used to check the stash list, which will return an output similar to the one below.

```
stash@{0}: WIP on main: abcdef1 Commit message
stash@{1}: WIP on feature: 1234567 Another commit message
stash@{2}: WIP on dev: 89abcde Yet another commit message
```

To check the changes in a specific stash entry, `git stash show -p stash@{0}` can be used (replace 0 for other entries in the list).
To make it easier to identify changes in the stash list, you can add a message when pushing to the stash using `-m`. For example:
`git stash -m "a message"`.

Once the stash entry to be applied has been identified, you can use `git stash apply stash@{0}` (again, 0 can be replaced for some other entry).
