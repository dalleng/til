# Customize directories where VSCode search for virtualenvs

If VSCode does not pick the directory where the virtualenv you want to use is located, which is sometimes the case with `poetry` created virtualenvs,
you can add the following key to your settings `python.venvPath` with the path to the folder where the virtualenvs are.

[Source](https://stackoverflow.com/a/59957906/238365)