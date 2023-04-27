# The comma operator (,)

The comma operator evaulates each of its operand from left to right, returning the result of the last.

For example:

```js
x = (1, 2, 4);
console.log(x); // prints 4
```

Can be very useful to quickly debug arrow functions not surrounded by brackets. For example, check the following JSX example.

```jsx
function InputWrapper() {
    return (
        <Input 
            onChange={(ev) => (console.log(ev), doSomething(ev))}
        />
    );
}
```

Sources:
- https://twitter.com/davidkpiano/status/1647258585187991552
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator
