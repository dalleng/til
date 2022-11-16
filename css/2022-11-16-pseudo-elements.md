# Pseudo-elements

A css pseudo-element is a keyword added to the selector to style a specific part of the selected element. For example, ::first-line which is used to style the first line of the selected element.

## Syntax

```css
selector::pseudo-element {
    property: value;
}
```

## Example

```css
p::first-line {
    text-transform: uppercase;
}
```

[Source](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)