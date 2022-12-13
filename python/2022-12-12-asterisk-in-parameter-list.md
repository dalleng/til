# What does an asterisk represent in the argument list of a function

A `*` is used to represent that all of the following arguments are keyword-only.

```python
In [7]: def test(positional, positional_or_keyword='foo', *, keyword_only='bar', keyword_only_no_default):
   ...:    print(f"position={positional}, positional_or_keyword={positional_or_keyword}, keyword_only={keyword_only}, keyword_only_no_default={keyword_only_no_default}")
   ...:

In [8]: test(10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[8], line 1
----> 1 test(10)

TypeError: test() missing 1 required keyword-only argument: 'keyword_only_no_default'

In [9]: test(10, 11)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[9], line 1
----> 1 test(10, 11)

TypeError: test() missing 1 required keyword-only argument: 'keyword_only_no_default'

In [10]: test(10, keyword_only_no_default=11)
position=10, positional_or_keyword=foo, keyword_only=bar, keyword_only_no_default=11

In [11]: test(10, keyword_only_no_default=11, positional_or_keyword=12)
position=10, positional_or_keyword=12, keyword_only=bar, keyword_only_no_default=11
```
