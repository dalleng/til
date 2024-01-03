# SSH Agent forwarding

SSH agent forwarding allows you to use private keys stored locally on a remote server.

## How to enable SSH agent forwarding

### Add keys to ssh-agent

`ssh-add ~/.ssh/id_rsa`

on macOS it is advised to use `-K` to save it on the Keychain, otherwise this setting isn't persisted
through reboots.

### Allow forwarding in your client's config.

In `~/.ssh/config`:

```
Host example
    ForwardAgent Yes
```

References:
- [What is SSH Agent Forwarding and How Do You Use It?](https://www.cloudsavvyit.com/25/what-is-ssh-agent-forwarding-and-how-do-you-use-it/)
- [Using SSH agent forwarding](https://docs.github.com/en/developers/overview/using-ssh-agent-forwarding)
