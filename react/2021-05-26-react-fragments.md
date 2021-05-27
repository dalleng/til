# React Fragments

Used to return a list of multiple elements with a generic enclosing component that doesn't
add any node to the DOM.

```jsx
render() {
  return (
    <React.Fragment>
      <ChildA />
      <ChildB />
      <ChildC />
    </React.Fragment>
  );
}
```

[Source](https://reactjs.org/docs/fragments.html#short-syntax)
