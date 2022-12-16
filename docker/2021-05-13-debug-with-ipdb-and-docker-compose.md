# Debugging with ipdb in a docker-compose environment

Enable interactive mode by adding the following lines to the service definition:

```yaml
version: 3
services:
    app:
        stdin_open: true
        tty: true
```

Run docker-compose detached with `docker-compose up -d` and attach to the container you set
the breakpoint in with `docker attach <container_name>`.

[Source](https://odwyer.software/blog/how-to-use-ipdb-with-docker-compose)
