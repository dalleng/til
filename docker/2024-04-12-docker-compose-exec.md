# `docker compose exec`

The same way you can use `docker exec` to execute a command on a container, `docker compose exec <service>` can be used
to execute a command on a container in the context of docker compose. For example:

Creating a superuser in a django project

```shell
docker compose exec -it <service_name> python manage.py createsuperuser
```

With `<service_name>` as defined in the compose file
