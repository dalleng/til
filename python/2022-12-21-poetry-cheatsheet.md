# Poetry Cheatsheet

## Existing Project

Execute the following to create the `pyproject.toml` file.

`poetry init`

## New Project

`poetry new foo`

Which will initialize the project with the following directory structure:

```bash
foo
├── README.md
├── foo
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py

2 directories, 4 files
```

A useful flag is `--src` which will nest the package inside the `src` folder resulting in the following directory structure:

```bash
foo
├── README.md
├── pyproject.toml
├── src
│   └── foo
│       └── __init__.py
└── tests
    └── __init__.py

3 directories, 4 files
```

## Create Virtual Env

`poetry install`

The command will read dependencies from `pyproject.toml` and install them. If there is no virtualenv activated, it will also create one. If there's no `poetry.lock` file it will create one.

## Install Packages

`poetry add flask`

adding the `--dev` parameter is used to mark a dependency as a development dependency.

## List dependencies

`poetry show`

show the dependency tree

`poetry show --tree`

## Update a dependency

`poetry update foo`

## Uninstall dependency

`poetry remove foo`