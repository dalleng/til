# `done` function in Jest tests

The `done` function can be useful for testing asynchronous code. Whenever `done` is passed to a test function, jest will
wait for `done` to be called before finishing the test or fail the test with a timeout error if `done` was
not called after a certain amount of time.

See the following example, in this case the test will finish before the callback is executed.

```javascript
// Don't do this!
test('the data is peanut butter', () => {
  function callback(error, data) {
    if (error) {
      throw error;
    }
    expect(data).toBe('peanut butter');
  }

  fetchData(callback);
});
```

We can make jest wait by using the `done` function. See:

```javascript
test('the data is peanut butter', done => {
  function callback(error, data) {
    if (error) {
      done(error);
      return;
    }
    try {
      expect(data).toBe('peanut butter');
      done();
    } catch (error) {
      done(error);
    }
  }

  fetchData(callback);
});
```

[Source](https://jestjs.io/docs/asynchronous#callbacks)
