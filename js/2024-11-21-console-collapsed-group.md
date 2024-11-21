# `console.groupCollapsed` function

`console.groupCollapsed` allows to create a group of `console.log()` logs that will be printed under a toggle.

## Example:

```js
console.groupCollapsed("Toggle me");
console.log("this will be inside the toggle");
console.log("something else");
console.groupEnd();
```