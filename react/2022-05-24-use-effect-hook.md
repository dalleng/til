# useEffect react hook

Using this hook tells React that it needs to do something after render. By default it runs after the first render
and after every update.

## Dependency array cheatsheet:
1. By default if no array is provided it is executed on mount and every render.
2. `[foo]` the effect will be called on first render and every time `foo` changes.
3. `[]` an empty dependency array will result in the effect function called only on mount.

[Source](https://react-hooks-cheatsheet.com/useeffect)
