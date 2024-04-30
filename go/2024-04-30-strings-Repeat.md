# `strings.Repeat` in go

Takes a string S and an int N as parameters, returns a new string with S repeated N times.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Repeat("foobar", 2))
}
```

[Source](https://pkg.go.dev/strings#Repeat)