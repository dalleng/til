# `Array.prototype.flatMap`

The flatMap method is a combination of calling map followed by flat. It simplifies the process of mapping over an array and flattening the result in one step.

Example

This method is particularly useful for extracting arrays from an array of objects and flattening the structure.

```js
const users = [
    {
        id: 1,
        roles: [1, 5, 8],
    },
    {
        id: 2,
        roles: [2, 3],
    },
];

const roles = users.flatMap((user) => user.roles);
console.log(roles);
// Output: [1, 5, 8, 2, 3]
```

[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
