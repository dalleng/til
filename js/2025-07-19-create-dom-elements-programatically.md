# Create DOM elements programatically

- Create a div in memory:

```js
const div = document.createElement('div');
```

- Set attributes and class:

```js
div.setAttribute('id', 'my-div');
div.className = 'my-class';
```

- Add it to the DOM:

```js
document.body.appendChild(div);
// or use any other container instead of body
document.querySelector('#element-with-id').appendChild(div);
```

- Clear the div’s contents:


- `div.innerHTML = ''` – clears all content
- `div.textContent = ''` – safer if just text
- `div.replaceChildren()` – modern & clean