# `useMemo` hook

The `useMemo` let's you cache computed values. The signature is the following:

```
useMemo(calculateValue, dependencies) 
```

Where `calculateValue` is the function that calculates the value to be cached, and `dependencies` the array of dependencies
react checks have changed in order to trigger a re calculation.

[Source](https://react.dev/reference/react/useMemo#usememo)