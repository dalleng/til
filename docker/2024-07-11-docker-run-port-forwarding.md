# Port forwarding in docker run

The `-p` flag can be used for forwarding a port from a container to the host.

```bash
docker run -p <host_port>:<container_port> <image>
```

[Docs](https://docs.docker.com/reference/cli/docker/container/run/#publish)