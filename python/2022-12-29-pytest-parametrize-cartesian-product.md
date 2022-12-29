# Using multiple `pytest.mark.parametrize` decorators

Multiple `pytest.mark.parametrize` decorators could be used in test functions to get the cartesian product of the parameters.

This snippet:

```python
import itertools
import pytest
​
numbers = [1,2,3,4,5]
vowels = ['a','e','i','o','u']
​
@pytest.mark.parametrize(
	itertools.product(number, vowels)
)
def test(number, vowel):
	...
```

is equivalent to this other snippet.

```python
import pytest
​
numbers = [1,2,3,4,5]
vowels = ['a','e','i','o','u']
​
@pytest.mark.parametrize('number', numbers)
@pytest.mark.parametrize('vowel', vowels)
def test(number, vowel):
    pass
```

[Source](https://stackoverflow.com/questions/22171681/parameterized-test-with-cartesian-product-of-arguments-in-pytest/)