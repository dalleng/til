# Doubly Linked List in Go

Go has a doubly linked list implementation in `container/list`.

Example:

```go
package main

import (
	"container/list"
	"fmt"
)

func main() {
	l := list.New()
	l.PushBack(9)
	l.PushBack(8)
	l.PushBack(7)
	for e := l.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}
    // Outputs
    // 9
    // 8
    // 7
}
```

[Docs](https://pkg.go.dev/container/list#Element)