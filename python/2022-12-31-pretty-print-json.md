# Pretty print JSON

`json.dumps` takes an optional keyword argument `indent` that makes the output string indented
at the level specified by the value passed.

```python
In [1]: import json

In [2]: d = {'foo': 'bar', 'jazz': [{'car': [{'bazz': 'fuzz'}]}]}

In [3]: json.dumps(d, indent=2)
Out[3]: '{\n  "foo": "bar",\n  "jazz": [\n    {\n      "car": [\n        {\n          "bazz": "fuzz"\n        }\n      ]\n    }\n  ]\n}'

In [4]: print(json.dumps(d, indent=2))
{
  "foo": "bar",
  "jazz": [
    {
      "car": [
        {
          "bazz": "fuzz"
        }
      ]
    }
  ]
}
```