# `Pick` generic

The `Pick` generic allows you to create a new type based on a subset of keys of an existing type. In the example below,
the `TodoPreview` type includes the `title` and `completed` keys from the `Todo` interface, but not `description`.

```
interface Todo {
    title: string;
    description: string;
    completed: boolean;
}

type TodoPreview = Pick<Todo, 'title' | 'completed'>;

let todo: TodoPreview = {
    title: 'Clean room',
    completed: false
};
```

In more detail: `Pick<T, K extends keyof T>` is a generic that takes two type arguments. `T` is the type from which you want
to pick properties. `K` is the properties you want to pick from `T`.
