# Customize iPython shell

You can add user-level customizations to the iPython shell by editing the following file in your home directory.

`~/.ipython/profile_default/ipython_config.py`

The file is not created by iPython during it's installation, so if it doesn't exist you need to create it. If you don't
have it execute the following:

```bash
ipython profile create
```

## Example of adding an alias to the iPython shell

```python
c.AliasManager.user_aliases = [("cl", "clear")]
```

[Docs](https://ipython.readthedocs.io/en/stable/config/intro.html)
