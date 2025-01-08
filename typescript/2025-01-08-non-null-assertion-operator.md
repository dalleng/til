# ! operator in typescript

In TypeScript, the ! operator, known as the non-null assertion operator, is used to tell the TypeScript compiler that a particular value is not null or undefined, even if it can’t be proven from the type system. It essentially asserts that the value is safe to use and bypasses the compiler’s strict null checks.

You place the ! operator immediately after a variable or expression.

```typescript
variable!;
```