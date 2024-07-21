# Docker compose watch

Compose watch lets you define how a service reacts to file changes in the host.

- It can be used as an alternative to bind mounts to sync code between host and container for development.
- It can used to trigger images to be rebuilt if there are changes to dependencies.
- It can be used to trigger containers to be restarted, which is useful for changes to configuration files.

Examples:

## Alternative to bind mount

```yaml
services:
  web:
    build: .
    ports:
      - "8000:5000"
    develop:
      watch:
        - action: sync
          path: .
          target: /code
  redis:
    image: "redis:alpine"
```

## Trigger image to be rebuilt

- The image is rebuilt if there are changes to `package.json`
- In this example another interesting feature being shown is the ability to excluce certain paths, in this case `node_modules`. 

```yaml
services:
  web:
    build: .
    command: npm start
    develop:
      watch:
        - action: sync
          path: ./web
          target: /src/web
          ignore:
            - node_modules/
        - action: rebuild
          path: package.json
```

## Sync and restart container

- The container restarts if there are changes to `nginx.conf`

```yaml
services:
  web:
    build: .
    command: npm start
    develop:
      watch:
        - action: sync
          path: ./web
          target: /app/web
          ignore:
            - node_modules/
        - action: sync+restart
          path: ./proxy/nginx.conf
          target: /etc/nginx/conf.d/default.conf

  backend:
    build:
      context: backend
      target: builder
```

[Docs](https://docs.docker.com/compose/file-watch/)