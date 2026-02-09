# Load or run python files from `ipython`

Let's say we have a file, `hello_world.py` with the following content.

```python
def main():
    print("Hello World")


if __name__ == "__main__":
    main()
```

## Import code into an `ipython` REPL

Use `%load` to load the file content into the REPL. It does not execute until you press enter. It is basically
like pasting the content of the file.

```shell
In [1]: %load hello_world.py

In [2]: # %load hello_world.py
   ...: def main():
   ...:     print("Hello World")
   ...:
   ...:
   ...: if __name__ == "__main__":
   ...:     main()
   ...:
Hello World
```

## Run code in the `ipython` REPL 

`%run` executes the code in the file directly without pasting its content into the REPL. 

```shell
In [1]: %run hello_world.py
Hello World
```