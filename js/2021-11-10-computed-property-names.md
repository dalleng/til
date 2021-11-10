# Computed property names

Starting with ECMAScript 2015, the object initializer syntax also supports computed property names.
That allows you to put an expression in brackets [], that will be computed and used as the property name.

```js
let param = 'size'
let config = {
  [param]: 12,
}
console.log(config); // {size: 12}
```

[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)
