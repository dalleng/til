# The `itemgetter` function from the `operator` module.

The `operator` module in the python standard library implements operators (+, -, >, < and several others) as functions.

`itemgetter` is a function that implements fetching elements from its operand. Similar to how `[]` is used to access
elements insides dictionaries or list using keys or indices. 

## Basic example

```python
la_liga_players = [
        {
            'name': 'Lamine Yamal',
            'number': 10,
            'team': {
                'name': 'FC Barcelona',
                'location': {
                    'city': 'Barcelona',
                    'country': 'Spain'
                }
            }
        },
        {
            'name': 'Mike Oyarzabal',
            'number': 10,
            'team': {
                'name': 'Real Sociedad',
                'location': {
                    'city': 'San Sebastian',
                    'country': 'Spain'
                }
            }
        }
]
# get a value using a list index
first_getter = itemgetter(0)
print(f"{first_getter(la_liga_players)=}", end='\n\n')

# get multiple values using list indices
first_and_second_getter = itemgetter(0, 1)
print(f"{first_and_second_getter(la_liga_players)=}", end='\n\n')

# get a value using a key dict
name_getter = itemgetter('name')
for player in la_liga_players:
    print(f"{name_getter(player)=}")

print()

# get multiple values using key dics
name_and_club_getter = itemgetter('name', 'team')
for player in la_liga_players:
    print(f"{name_and_club_getter(player)=}")
```

**Output**

```shell
first_getter(la_liga_players)={'name': 'Lamine Yamal', 'number': 10, 'team': {'name': 'FC Barcelona', 'location': {'city': 'Barcelona', 'country': 'Spain'}}}

first_and_second_getter(la_liga_players)=({'name': 'Lamine Yamal', 'number': 10, 'team': {'name': 'FC Barcelona', 'location': {'city': 'Barcelona', 'country': 'Spain'}}}, {'name': 'Mike Oyarzabal', 'number': 10, 'team': {'name': 'Real Sociedad', 'location': {'city': 'San Sebastian', 'country': 'Spain'}}})

name_getter(player)='Lamine Yamal'
name_getter(player)='Mike Oyarzabal'

name_and_club_getter(player)=('Lamine Yamal', {'name': 'FC Barcelona', 'location': {'city': 'Barcelona', 'country': 'Spain'}})
name_and_club_getter(player)=('Mike Oyarzabal', {'name': 'Real Sociedad', 'location': {'city': 'San Sebastian', 'country': 'Spain'}})
```

## Advanced example

The example below shows the implementation of a function that can follow and retrieve elements from a nested object
composed of dictionaries and lists.

```python
def nestedgetter(obj: list | dict, items: list):
    """
    Retrieve a nested value from a list/dict structure by successively
    applying keys or indices.

    Starting from `obj`, each element in `items` is applied in order using
    `operator.itemgetter`, so each key/index is looked up on the result of
    the previous step.

    This is equivalent to:
        result = obj
        for key in items:
            result = result[key]

    Parameters
    ----------
    obj : list | dict
        The root object to traverse. Must support indexing via `[]`.
    items : list
        A sequence of keys or indices used to access nested elements.

    Returns
    -------
    Any
        The value found at the nested path defined by `items`.

    Raises
    ------
    KeyError
        If a key is missing in a dictionary.
    IndexError
        If an index is out of range in a list.
    TypeError
        If an intermediate value does not support indexing.
    """
    return reduce(lambda result, key: itemgetter(key)(result), items, obj)


print(f"{nestedgetter(la_liga_players, [0, 'name'])=}")
print(f"{nestedgetter(la_liga_players, [1, 'team', 'location', 'city'])=}")
```

Output

```shell
nestedgetter(la_liga_players, [0, 'name'])='Lamine Yamal'
nestedgetter(la_liga_players, [1, 'team', 'location', 'city'])='San Sebastian'
```
