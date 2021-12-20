# Multiple SSH Keys for different Github Accounts

Assuming you have different ssh keys you need to use because you have multiple
github accounts or different keys for different repos, you can add multiple configurations
to `~/.ssh/config`.

All keys should be already added to the ssh-agent using `ssh-add ~/.ssh/key` (use `-K` in macOS).

In `~/.ssh/config`:

```
Host example1
    HostName github.com
    User git
    IdentityFile ~/.ssh/a_key

Host example2
    HostName github.com
    User git
    IdentityFile ~/.ssh/another_key
```

Also, make sure the `origin` remote in `.git/config` uses the Host defined `~/.ssh/config`.

For example, for the example1 entry:

```
[remote "origin"]
    url = git@example1:account/project.git
```
