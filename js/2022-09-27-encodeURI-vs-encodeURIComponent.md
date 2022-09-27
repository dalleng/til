# JS `encodeURI` and `encodeURIComponent` functions

The `encodeURI()` function encodes a URI by replacing each instance of certain characters by one, two, three,
or four escape sequences representing the UTF-8 encoding of the character.

The `encodeURI()` function does not encode characters that have special meaning (reserved characters) for a URI.

`encodeURI()` escapes all characters except:

```
Not Escaped:
    A-Z a-z 0-9 ; , / ? : @ & = + $ - _ . ! ~ * ' ( ) #
```

Note that `encodeURI()` by itself cannot form proper HTTP GET and POST requests, such as for `XMLHttpRequest`,
because &, +, and = are not encoded, which are treated as special characters in GET and POST requests.
`encodeURIComponent()`, however, does encode these characters.

```js
const set1 = ";,/?:@&=+$#"; // Reserved Characters
console.log(encodeURI(set1)); // ;,/?:@&=+$#
console.log(encodeURIComponent(set1)); // %3B%2C%2F%3F%3A%40%26%3D%2B%24%23
```

TL;DR Use `encodeURIComponent` if portions of the HTTP request, for example query string parameters, can contain
special characters as part of the data and you want to properly escape them.

- [Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#encodeuri_vs_encodeuricomponent)
