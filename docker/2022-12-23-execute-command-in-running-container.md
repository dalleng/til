# Execute command in running container

`docker exec` lets you run commands in a running container. For example, to get a bash prompt you would do:

`docker exec -it <container> bash`

|flag|description|
|---|---|
|`-i`|Keep STDIN open even if not attached|
|`-t`|Allocate a pseudo-TTY|

For docs and complete list of flags: https://docs.docker.com/engine/reference/commandline/exec/