# `utf8.RuneCountInString` utility function to count runes in a string.

In Go, if you do `len(string)` you get the byte size which might not always match the character count. For example,
if you execute `len("niño")` you will get `5`, since `ñ` is a non ascii character and takes more than one byte to encode.
The recommended thing to do in cases in which you need to access strings by characters is to first cast the `string` to a
`rune` slice, for example `len([]rune("niño"))` which would the return `4`. An alternative to this is to use the function 
`RuneCountInString` from `unicode/utf8` in the standard library.


```go
package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	foo := "niño"
	fmt.Println(len(foo))                    // prints 5 as len returns the byte count and ñ is non ascii
	fmt.Println(len([]rune(foo)))            // prints 4 as the strings is casted to a rune slice first
	fmt.Println(utf8.RuneCountInString(foo)) // utility function to return the rune count
}
```

[Source](https://pkg.go.dev/unicode/utf8#RuneCountInString)