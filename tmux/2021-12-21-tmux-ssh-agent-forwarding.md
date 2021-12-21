# Reconciling Tmux and SSH Agent Forwarding.

SSH agent forwarding creates a socket file and stores the path in `SSH_AUTH_SOCK`. In between
reconnections tmux panes or windows could be left with a stale value in `SSH_AUTH_SOCK` leading
to ssh connection errors. For example, authentication errors when trying to push/pull to a git repo.

To make sure `SSH_AUTH_SOCK` always points to the right socket:

1. Create a symlink on ssh connection. In `~/.ssh/rc`.

```bash
#!/bin/bash

# Fix SSH auth socket location so agent forwarding works with tmux
if test "$SSH_AUTH_SOCK" ; then
    ln -sf $SSH_AUTH_SOCK ~/.ssh/ssh_auth_sock
fi
```

2. Set `SSH_AUTH_SOCK` to the symlink in tmux. In `~/tmux.conf`.

```
# Remove SSH_AUTH_SOCK to disable tmux automatically resetting the variable
set -g update-environment "DISPLAY SSH_ASKPASS SSH_AGENT_PID \
                             SSH_CONNECTION WINDOWID XAUTHORITY"

# Use a symlink to look up SSH authentication
setenv -g SSH_AUTH_SOCK $HOME/.ssh/ssh_auth_sock
```

Source: [Reconciling Tmux and SSH Agent Forwarding.](https://blog.testdouble.com/posts/2016-11-18-reconciling-tmux-and-ssh-agent-forwarding/)
