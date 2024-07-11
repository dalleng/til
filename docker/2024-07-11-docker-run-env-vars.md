# Setting environment variables in a container with docker run

When running a container with docker run you can pass environment variables using the `-e` flag.

```bash
docker run -e VAR=foo <image>
```

[Docs](https://docs.docker.com/reference/cli/docker/container/run/#env)