# Using `unittest.mock.patch` as a class decorator

When applying the `unittest.mock.patch` decorator at the class level, all test methods get the mock as an
argument. See example below:

```python
import unittest
import unittest.mock


def print_greeting(name):
    print(f"hello {name}!")


@unittest.mock.patch("builtins.print")
class SampleTest(unittest.TestCase):

    def test1(self, mock_print):
        name = "diego"
        print_greeting("diego")
        mock_print.assert_called_with(f"hello {name}!")

    def test2(self, mock_print):
        name = "allen"
        print_greeting("allen")
        mock_print.assert_called_with(f"hello {name}!")


if __name__ == '__main__':
    unittest.main()
```