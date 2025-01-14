# Built-in data structures

Python comes with powerful data structures built in to the language. They form a rich variety of ways to organise, group, store and find data.

## Tuple

A tuple is a simple group of values. The values may or may not be related to each other, although it is less mind-bending if they are related.

```python
favouriteFoods = ("eggs", "sausage", "chips", "beans")
print(favouriteFoods)
```

The purpose of a tuple is to package up data items that need to be considered as a single whole. If data is always used together, and needs to be represented as a single thing, a tuple might be the way to represent that data.

### Reading tuple values

We use a zero-based index:

```python
favouriteFoods = ("eggs", "sausage", "chips", "beans")

print(favouriteFoods[0])
print(favouriteFoods[1])
print(favouriteFoods[2])
print(favouriteFoods[3])
```

> Caution: This can be hard to read. What does index 2 represent, exactly?

Tuples can be unpacked:

```python
favouriteFoods = ("eggs", "sausage", "chips", "beans")
(foodA, foodB, foodC, foodD) = favouriteFoods
print("unpacked:", foodA, foodB, foodC, foodD)
```

### Tuple properties

Tuples are

- Ordered: the order of values will not change
- Immutable: the values are read-only and cannot be changed
- Allowed duplicate values: the same value can appear more than once
- Joinable: tuples can be joined together using `+`

If you try to modify a value, Python produces this error message:

```text
TypeError: 'tuple' object does not support item assignment
```

### Iterating over a tuple

We can iterate over values:

```python
favouriteFoods = ("eggs", "sausage", "chips", "beans")
for food in favouriteFoods:
    print("Iterate tuple:", food)
```

## List

Lists are Python's approach to dynamic arrays that can contain a number of elements and can grow and shrink in size. Lists are a widely used building block in Python.

### Create a list

```python
users = ["alan", "beth", "chris"]
print(users)
```

Note the square brackets to define the list values.

### Iterating over a list with for

The `for` keyword will happily iterate over elements in a list:

```python
users = ["alan", "beth", "chris"]

for user in users:
    print(user)
```

### Read a list element

```python
# List
users = ["alan", "beth", "chris"]
print(users)
```

```python
# Iterate list
users = ["alan", "beth", "chris"]

for user in users:
    print("Iterate list:", user)

# List CRUD - create list
users = ["alan", "beth", "chris"]
print("Original list:", users)

# Read list element by zero based index
firstUser = users[0]
print("read by index", firstUser )

# Read Negative index counts from end of list
lastUser = users[-1]
print("read by negative index", lastUser)

# Update element value
users[1] = "barry"
print( "Modify list element", users[1])
```

### Delete element by index

Individual elements can be deleted from the list using their index and `pop()`:

```python
users = ["alan", "beth", "chris"]
users.pop(1)
print("delete (index)", users)
```

### Delete element by value

Elements can be deleted by their value:

```python
users = ["alan", "beth", "chris"]
users.remove("alan")
print("delete (value)", users)
```

### Delete by value removes only first value

When deleting by value, only the _first_ occurrence from the start of the list will be removed:

```python
users = ["alan", "beth", "chris", "alan"]
users.remove("alan")
print("delete (first value)",users)
```

### Delete last element

The final element of a list can be removed using `pop()` with no arguments:

```python
users = ["alan", "beth", "chris"]
users.pop()
print("delete last element", users)
```

### Joining lists

Single elements can be appended to the end of a list:

```python
# Append element to end
users = ["alan", "beth", "chris"]
users.append("danielle")
print(users)
```

Entire lists can be joined, using the + operator:

```python
# Join lists
new_users = ["dave", "erica"]

users = ["alan", "beth", "chris"]
updated_users = users + new_users
print(updated_users)
```

Lists have more useful methods on them, such as `reverse()`. You can find out more at [Python docs](https://docs.python.org/3/tutorial/datastructures.html)

### List comprehension

Python's power tool for lists - the list comprehension.

Here is an example to collect users whose names begin with the letter "a", possibly useful for a [database shard](<https://en.wikipedia.org/wiki/Shard_(database_architecture)>):

```python
users = ["alan", "aaron", "alicia", "beth", "chris"]
users_shard_a = [u for u in users if u.startswith("a")]
print(users_shard_a)
```

Which shows:

```text
['alan', 'aaron', 'alicia']
```

A list comprehension will

- return a new list
- based on an existing list
- after applying some filtering or modifying function
- in a one-line syntax

#### Filtering

#### Using lambda syntax

#### Sorting

## Dictionary

### CRUD operations

### Lookup usage

## Set

# Next

[05-???]()

[Back to contents](/contents.md)
