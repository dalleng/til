# `Array.prototype.flat` to flatten nested arrays.

The flat method returns a new array with the subarrays of the original array concatenated into it. It takes an optional depth parameter, which specifies how deeply nested arrays should be flattened. The default value of depth is 1.

## Examples:

- With the default value of `depth`

```js
> const foo = [1, [2, 3], [4, 5], [[6]]];
> console.log(foo.flat());
[ 1, 2, 3, 4, 5, [ 6 ] ]
```

- Explicitly setting `depth`

```js
> console.log(foo.flat(2));
[ 1, 2, 3, 4, 5, 6 ]
```

[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)