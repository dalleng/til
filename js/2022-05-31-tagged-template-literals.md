# Tagged Template Literals

This feature enables us to apply a tag to template literals, thereby allowing us to execute a function on the template literal and have control over variable substitution.
See the following example.

```javascript
function bold(strings, ...values) {
    str = '';
    strings.forEach((string, i) => {
        // surrounding text with ** makes it bold in markdown
        str += string + (values[i] ? `**${values[i]}**` : '')
    });
    return str;
}

const name = "Diego"
console.log(bold`My name is ${name}`); // prints 'My name is **Diego**'
```

[Source](https://wesbos.com/tagged-template-literals)