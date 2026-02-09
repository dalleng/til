# `box-sizing: border-box` in CSS

In CSS the default behavior is that padding and borders make elements take more space. For example:

```css
div {
  width: 200px;
  border: 10px solid black;
}
```

The rendered div will actually be of `220px` of height and width.

The behavior most people expect of padding and borders being part of the height and width defined is achieve by using `box-sizing: border-box`. With `box-sizing: border-box`:

- Width and height include content + padding + border
- Adding a border does not increase the outer size
- Content shrinks instead

## Set predictable layouts

The snippet below applies `box-sizing: border-box` to all layout boxes making widht and height predictable.

```
*,
*::before,
*::after {
  box-sizing: border-box;
}
```