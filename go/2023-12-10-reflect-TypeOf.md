# Use `reflect.Typeof` get the type of a variable

The `reflect.Typeof` function of the `reflect` package in go
lets you determine the type of a variable at runtime. See example below:

```go
package main

import (
    "fmt"
    "reflect"
)

func main() {
    a := 42
    b := "hello"
    c := 3.14
    d := true

    fmt.Println(reflect.TypeOf(a)) // int
    fmt.Println(reflect.TypeOf(b)) // string
    fmt.Println(reflect.TypeOf(c)) // float64
    fmt.Println(reflect.TypeOf(d)) // bool
}
```