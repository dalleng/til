# Fixing commits with `git commit --fixup` and `git rebase -i --autosquash`

`git commit --fixup` is very useful if you want to do fixes and later rewrite history to make it look like the fix was already in the original commit.

`git commit --fixup <sha>` associates a new commit with a previous commit, so that it's easier to squash them when doing a interactive rebase. It automatically reorder commits in interactive rebases so the original commit and the fixup are already one after the other.

`git rebase -i --autosquash <sha>` goes one step ahead and it automatically squashes original commits and their fixups.

