# Rebase when pulling

When pulling from a remote branch, and the branches differ, rebase instead of merging.

`git pull --rebase`

Setting it as the default behavior:

`git config --global pull.rebase true`