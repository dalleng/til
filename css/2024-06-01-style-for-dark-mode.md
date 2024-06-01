# Add style rules for dark mode

The `@media (prefers-color-scheme: dark)` rule can be used to specify styles that should
only be applied when dark mode is enabled.

```css
/* Dark mode styles */
@media (prefers-color-scheme: dark) {
  body {
    background-color: black;
    color: white;
  }
}
```