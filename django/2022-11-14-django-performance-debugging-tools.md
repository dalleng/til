# Django performance debugging tools

Compendium of django debugging packages.

## Django Debug Toolbar

Displays a configurable set of panels on django rendered views. Panels display executed queries, cache calls, signals, cpu time.
Very useful to debug perfomance issues. Custom panels can be added as well. The only con of this project is that it only works
on Django rendered views as the debug panel is added using django templates.

If Django Rest Framework is used, the browsable API can be used to render the debug panel and inspect REST API requests.

[https://github.com/jazzband/django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)

## Django Silk

Silk intercepts and stores HTTP requests and database queries before presenting them in a user interface for further inspection. Very useful to debug Ajax calls and APIs.

The only con of this project is that it stores http requests and queries in the DB, which can make the application slower if enabled on prod. Of course, an option would be to only enable it on development environments.

(https://github.com/jazzband/django-silk)[https://github.com/jazzband/django-silk]

## Django Query Inspect

Logs repeated queries to the console. It can also display a traceback to where the queries occur in the codebase.
(https://github.com/dobarkod/django-queryinspect)[https://github.com/dobarkod/django-queryinspect]
