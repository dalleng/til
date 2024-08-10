# Escape sequence to add emojis to javascript strings

In JS strings you can use the escape sequence '\u' to add unicode characters.

Examples:

For the [snake emoji](https://codepoints.net/U+1f40d).

- Using the code points directly

```javascript
> console.log('\u{1f40d}')
🐍
```

- Using UTF-16


```javascript
> console.log('\ud83d\udc0d')
🐍
```
