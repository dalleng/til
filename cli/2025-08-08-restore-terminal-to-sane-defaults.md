# Use `stty sane` to restore terminal

`stty sane` restores the terminal to its default “sane” settings. I find it particularly useful when a process changes the terminal configuration and doesn’t reset it on exit.  
A common symptom is that pressing `Ctrl+C` no longer sends `SIGINT` to the foreground process — instead, `^C` is echoed to the screen because signal generation (`isig`) was disabled.