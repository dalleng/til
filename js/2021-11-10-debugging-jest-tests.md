# Debugging jest tests with breakpoints.

Place a `debugger;` statement in any of your testsce a debugger; statement in any of your tests. Then when running
the test suite use the `--inspect-brk` flag.

```
node --inspect-brk node_modules/.bin/jest --runInBand [any other arguments]
```

To debug in Google Chrome (or any Chromium-based browser), open your browser and go to chrome://inspect and
click on "Open Dedicated DevTools for Node".

[Source](https://jestjs.io/docs/troubleshooting)
