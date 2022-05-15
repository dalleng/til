# JS Promises.

A promise represents the eventual successful (or unsuccessful) completion of an asynchronous operation.

How to define a Promise:

```js
const myPromise = new Promise((resolve, reject) => {
    try {
        const result = asyncOperation();
        resolve(result);
    } catch(err) {
        reject(`asyncOperation failed: ${err}`);
    }
});
```

Basic usage:

```js
myPromise.then(resolveCallback, rejectCallback); // resolve and reject callback
myPromise
    .then(resolveCallback) // successful callback
    .catch(rejectCallback) // error callback
    .finally(finallyCallback); // callback always executed
```

Async/Await usage:

```js
async function() {
    try {
        const result = await myPromise;
    } catch(err) {
        // handle err
    }
}
```
