# Reload tmux configuration

## From the command line

`tmux source-file <path>`

## From inside a tmux session

`source-file <path>`

## Creating a keyboard shortcut to reload

Add the following to bind `prefix + r` to reload the `.tmux.conf` file in the home
directory

```
bind r source-file ~/.tmux.conf
```
