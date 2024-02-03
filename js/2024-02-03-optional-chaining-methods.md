# Optional chaining with methods in JS

`object?.method()` does not execute anything nor throw any errors if `object` is `undefined` or `null`, or `method` is not a function or is not defined for `object`.

This greatly simplifies error handling and checking 