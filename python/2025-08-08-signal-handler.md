# Setting a signal handler

Using the [`signal`](https://docs.python.org/3/library/signal.html#signal.signal) function in the [`signal`](https://docs.python.org/3/library/signal.html) module you can write a custom handler for unix process signals.

```python
import sys
import signal
from time import sleep


def main():
    def _sigint_handler(sig, frame):
        print("SIGINT has been recevied", flush=True)
        sys.exit(0)

    signal.signal(signal.SIGINT, _sigint_handler)

    print("Executing... Press Ctrl+C to stop...", flush=True)
    while True:
        sleep(1)


if __name__ == "__main__":
    main()
```