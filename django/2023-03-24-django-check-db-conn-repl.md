# Check the database connection settings from the Django shell

When connected to a Django shell, after executing `python manage.py shell`. You can execute the following snippet
to obtain the DB connection settings.

```
from django.db import connection
print(connection.settings_dict)
```

which is going to return a dictionary similar to this one:

```
{'ENGINE': 'django.db.backends.postgresql',
 'HOST': 'localhost',
 'NAME': '************',
 'PASSWORD': '********',
 'PORT': '5432',
 'USER': '************',
 'ATOMIC_REQUESTS': False,
 'AUTOCOMMIT': True,
 'CONN_MAX_AGE': 0,
 'OPTIONS': {'fallback_application_name': 'django_shell'},
 'TIME_ZONE': None,
 'TEST': {'CHARSET': None,
  'COLLATION': None,
  'MIGRATE': True,
  'MIRROR': None,
  'NAME': None}}
```