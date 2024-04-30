# `slices.Reverse`

Reverses a slice in-place.

```go
package main

import (
	"fmt"
	"slices"
)

func main() {
	numbers := []int{2, 3, 4, 5}
	slices.Reverse(numbers)
	fmt.Println(numbers) // prints [5 4 3 2]
}
```

[Source](https://pkg.go.dev/slices#Reverse)