# Nullish coalescing operator (??)

Returns the value on the right hand side if the value on the left hand side is `null` or `undefined`. Useful
when you need to choose between a provided value or a default, but falsy values like `0` or `''` are valid
options.

```nodejs
> 0 ?? 'won\'t use this value'
0
> false ?? 'won\'t use this value'
false
> undefined ?? 'will use this value'
'will use this value'
> null ?? 'will use this value'
'will use this value'
```

Differs from `||` which returns the value on the right hand side if the value on the left hand side is falsy.

[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
