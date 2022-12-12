# What does an asterisk represent in the argument list of a function

A `*` is used to represent that all of the following arguments are keyword-only.

```python
In [1]: def test(positional, positional_or_keyword='foo', *, keyword_only='bar', keyword_only_no_default):
   ...:     print(f"position={positional}, positional_or_keyword={positional_or_keyword}, keyword_only={keyword_only}")
   ...:

In [2]: test(10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[2], line 1
----> 1 test(10)

TypeError: test() missing 1 required keyword-only argument: 'keyword_only_no_default'

In [3]: test(10, 11)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[3], line 1
----> 1 test(10, 11)

TypeError: test() missing 1 required keyword-only argument: 'keyword_only_no_default'

In [4]: test(10, keyword_only_no_default=11)
position=10, positional_or_keyword=foo, keyword_only=bar

In [5]: test(10, keyword_only_no_default=11, positional_or_keyword='jazz')
position=10, positional_or_keyword=jazz, keyword_only=bar
```