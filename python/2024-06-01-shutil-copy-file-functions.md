# File copy functions in `shutil`

There are different utility functions in the `shutil` module of the standard library for copying files. 

- `copyfile(src, dst, *, follow_symlinks=True)` both `src` and `dst` can be either `str`
or a path like object (for example, `pathlib.Path`). `dst` needs to be a file path, not a destination directory. Only copies file content, does not copy metadata.

- `shutil.copy(src, dst, *, follow_symlinks=True)` both `src` and `dst` can be either `str` or a path like object (for example, `pathlib.Path`). `dst` can be either a file path or the destination directory. Returns the path to the newly created file. Copies data and permissions, but does not copy other metadata like file creation and modification times. If you want to preserve all metadata use `shutil.copy2(src, dst, *, follow_symlinks=True)`

[Source](https://docs.python.org/3/library/shutil.html)