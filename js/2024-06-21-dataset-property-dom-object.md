# Get the data attributes of a DOM element with javascript

```html
<div id="aDiv" data-foo="bar">
```

```js
const cell = document.getElementById('aDiv');
console.log(cell.dataset); // returns DOMStringMap {foo: 'bar'}
```