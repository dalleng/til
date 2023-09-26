# `useCallback`

Let's you cache a function definition so it isn't redefined after re-renders. The second argument of `useCallback` is a dependency list, if elements
of the dependency list change the function would re-defined. On each call to `useCallback` react checks for changes in elements in the dependency list,
if those haven't changed since the last render `useCallback` returns the cached function definition.

[Source](https://react.dev/reference/react/useCallback)