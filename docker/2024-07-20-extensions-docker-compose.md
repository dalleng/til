# Extensions in the compose file

Use keys with the prefix `x-` as a top level element to modularize configurations you want to reuse. Docker compose
ignores any fields that start with `x-`.

Extensions can be combined with anchors and aliases, to reference the shared configuration in different services. Check the following example.

```yaml
x-shared-env: &env
    - CONFIG_KEY
    - EXAMPLE_KEY

services:
    backend:
        <<: &env
        image: django:latest
    db:
        <<: &env
        image: postgres:latest
```

Keys starting with `x-` can also be used within other compose structures where user-defined keys are not expected. They can serve as metadata for custom scripts or other tools.

```yaml
service:
  backend:
    deploy:
      placement:
        x-aws-role: "arn:aws:iam::XXXXXXXXXXXX:role/foo"
        x-aws-region: "eu-west-3"
        x-azure-region: "france-central"
```

[Docs](https://docs.docker.com/compose/compose-file/11-extension/)