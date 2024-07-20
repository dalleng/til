# Using YAML anchors and aliases in docker compose files

In docker compose files you can use YAML anchors and aliases to avoid repetition. In the example below an anchor is defined using `&`
with an alias name, in this case `&django`. The alias is then referenced in the `celeryworker` service definition, using `<<: *django`.

The `<<:` override syntax allows for keys to be overriden. When there are repeated keys, the configuration specified directly within
the service will take precedence over the values inherited from the anchor.

```yaml
services:
    django: &django
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
        - .:/app/
        ports:
        - 8000:8000
        env_file:
        - .env

  redis:
    image: redis:7.2.4

  celeryworker:
    <<: *django
    depends_on:
      - redis
    ports: []
    command: python -m celery -A config worker -l info
```

[Docs](https://docs.docker.com/compose/compose-file/10-fragments/)