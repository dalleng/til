# `log.Fatalln` and `log.Fatalf`

Besides the `log.Fatal` function, there are also: 

- `log.Fatalln`

Equivalent to calling `Println` and then `os.Exit(1)`

- `log.Fatalf`

Equivalent to calling `Printf` and then `os.Exit(1)`