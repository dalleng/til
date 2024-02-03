# Using the `as` operator for mocks in jest tests

When using mocks or spys, and trying to call methods on those, typescript complains that the methods do not exists for those types.

The following can be fixed by forcing typescript to treat those objects as `jest.Mock` or `jest.SpyInstance` using the `as` operator.

```typescript
import { foo } from 'a/package';

jest.mock('a/package');

// Otherwise TS would throw an error saying mockReturnValue does not exits
const foo = jest.fn() as jest.Mock;
foo.mockReturnValue('some value'); 

// For spies you can use
const mySpy = jest.spyOn(someObject, 'someMethod') as jest.SpyInstance;
```