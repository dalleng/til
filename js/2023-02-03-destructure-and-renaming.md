# Destructure and renaming in ES6

- Destructure

```javascript
> const profile = { 'first_name': 'John', 'last_name': 'Doe' }
undefined
> const { first_name, last_name } = profile;
undefined
> first_name
'John'
> last_name
'Doe'
```

- Destructure and renaming

```javascript
> const profile = { 'first_name': 'John', 'last_name': 'Doe' }
undefined
> const { first_name: name, last_name: lastname } = profile;
undefined
> name
'John'
> lastname
'Doe'
```

[Source](https://wesbos.com/destructuring-renaming)
