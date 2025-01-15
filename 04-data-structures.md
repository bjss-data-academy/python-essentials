# Built-in data structures

Python comes with powerful data structures built in to the language. They form a rich variety of ways to organise, group, store and find data.

Code for this section can be found at [src/data-structures.py](/src/data-structures.py)

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

There is also a star (\*) syntax that can be used to unpack multiple elements into a list.

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

Find out more at [Python tuple docs](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

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

List elements can be read by using a zero-based index from the start of the list:

```python
# List
users = ["alan", "beth", "chris"]

# Read list element by zero based index
firstUser = users[0]
print(firstUser )
```

A negative index will read an element relative to the end of the list:

```python
users = ["alan", "beth", "chris"]
lastUser = users[-1]
print(lastUser)
```

### Update element value

Lists can have their element values changed:

```python
users = ["alan", "beth", "chris"]

users[1] = "barry"
print(users[1])
```

### Delete element by index

Individual elements can be deleted from the list using their index and `pop()`:

```python
users = ["alan", "beth", "chris"]
users.pop(1)
print(users)
```

### Delete element by value

Elements can be deleted by their value:

```python
users = ["alan", "beth", "chris"]
users.remove("alan")
print(users)
```

### Delete by value removes only first value

When deleting by value, only the _first_ occurrence from the start of the list will be removed:

```python
users = ["alan", "beth", "chris", "alan"]
users.remove("alan")
print(users)
```

### Delete last element

The final element of a list can be removed using `pop()` with no arguments:

```python
users = ["alan", "beth", "chris"]
users.pop()
print(users)
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

### List sort

Lists have a method `sort()` which does what it says on the tin:

```python
users = ["alan", "chris", "george", "frank", "beth"]
users.sort()
print (users)
```

Other options are availble by using arguments to sort(). See [Python list docs](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) for details.

## Dictionary

Another major data structure in Python is the dictionary. This is a key-value store.

### Create a dictionary

Here is a map used to look up email addresses for a username:

```python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

print(email_by_name)
```

The key is written on the left of the colon. The associated value is on the right.

### Lookup a dictionary value using the key

Individual values can be looked up efficiently by the key:

```python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

rosie_email = email_by_name["rosie"]
print(rosie_email)
```

### Update a dictionary value

We can update the value for a given key:

```python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

email_by_name["rosie"] = "new_email_rosie@example.com"
rosie_email = email_by_name["rosie"]
print(rosie_email)
```

### Delete a dictionary value

Deleting a key-value pair is easy enough:

```python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

email_by_name.pop("rosie")
print(email_by_name)
```

### Add a dictionary value

Adding a key-value pair is done with the square bracket syntax:

```python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

email_by_name["jenna"] = "jen@example.com"
print(email_by_name)
```

### Loop through dictionary keys

We can iterate over the keys in a dictionary:

````python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

for name in email_by_name.keys():
    print(name)```
````

giving

```text
alan
rosie
```

### Loop through dictionary values

We can iterate over the values in a dictionary:

````python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

for email in email_by_name.values():
    print(email)```
````

giving

```text
alan@example.com
rosie@example.com
```

### Loop through dictionary key-value pairs

Using `items()` to iterate over a dictionary returns tuples. We can unpack the tuples into key:value parts in the for loop:

```python
email_by_name = {
    "alan":  "alan@example.com",
    "rosie": "rosie@example.com"
}

for name, email in email_by_name.items():
    print("name", name, "email", email)
```

### Dictionaries can contain any python data

Dictionary values can themselves be tuples, lists, sets, or other dictionaries. Complex data structures can be built in this way.

Find out more at [Python dictionary docs](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Set

Sets contain data values where no two values can be the same.

### Create a set

We can create a set using the curly bracket notation:

```python
user_ids = {1001, 1002, 1004, 1000}
print("user ids", user_ids)
```

### Iterate over set values

Sets are iterated using `for`:

```python
user_ids = {1001, 1002, 1004, 1000}

for id in user_ids:
    print("user id", id)
```

### Test set contains value

Check that a value is contained in a set using `in`:

```python
user_ids = {1001, 1002, 1004, 1000}

if 1002 in user_ids:
    print("user id 1002 is known")

    user_ids.add(1002)
    print("Add id 1002 - no change", user_ids)
```

### Test set does not contain value

Test a value is not conatined using `not in`:

```python
user_ids = {1001, 1002, 1004, 1000}

if 1003 not in user_ids:
    print("user id 1003 not known")

    # Add value
    user_ids.add(1003)
    print("Added id 1003", user_ids)

    # Remove value
    user_ids.remove(1003)
    print("Removed id 1003", user_ids)
```

### Set based methods

The set data type has a number of set-theory based methods.

These allows us to find the intersection of two sets, the union of two sets, join sets and more. These methods are very useful in data engineering applications.

Find out more details at the [Python set docs](https://docs.python.org/3/tutorial/datastructures.html#sets)

# Next

[05-???]()

[Back to contents](/contents.md)

```

```

```

```
