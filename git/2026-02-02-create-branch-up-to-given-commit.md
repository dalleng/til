# Create a branch at a given commit

## Creates a branch in which the newest commit is `<commit_hash>`

The `-b` flag to create the branch and switch it to it immediately.

`git branch -b <branch_name> <commit_hash>`

## Creates a branch up to, but not including `<commit_hash>`

See the `^` after the `<commit_hash>`.

`git branch -b <branch_name> <commit_hash>^`