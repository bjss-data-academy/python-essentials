# Python objects and Object Oriented basics

Objects in Python are a way to bring together code with the data it works on.

Objects form a nice way to organise code. They naturally split a large program up into smaller building blocks. This approach is known as Object Oriented Programming or OOP.

Knowing how to use objects is essential to get the best out of Python and tools like PySpark.

Code for this section is at [src/objects.py](/src/objects.py)

## Create a class

Let's write some code to greet users of our system with a cheery message. We will use OO to do this.

We will end up with a separate object for each user in our system.

Each one of our user objects shares things in common: the data about a user's name, and the logic to print a greeting message. We write this common code in a _class_. Python uses _class-based_ OO.

A class is a blueprint from which we create all related objects.

Once we have a class, we can make as many user objects as memory allows.

Let's write a class suitable for greeting our users. We will name it class `User`:

```python
class User:
  def __init__(self, name):
    self._name = name

  def greet(self):
    greeting = "Welcome to Data Engineering, " + self._name
    print(greeting)
```

We start with the keyword `Class` and the name of the class. We'll call it `User` as this class describes behaviour surrounding our users.

You'll see the keyword `def` used indented inside the class.

Normally, `def` defines functions. In a class, these functions are called _methods_ and they are slightly different to normal functions:

- They always have a first parameter called `self`
- A method has access to all the data in the object instance

We see two methods with names `__init__` and `greet`.

Method `__init__` is known as a _constructor_. A constructor has one job: to get an object instance ready to use. To do this, it creates space in memory for the object to live. The code inside the constructor must then initialise the data values in that object.

For `User` objects, each object has just one data value. This is stored in a _field_ called `_name`. This is a variable that belongs to each individual object we make. Each object has its own, unique `_name` field.

### Create an object

Let's create an object instance of class User (we term this _a user object_ as shorthand jargon):

```python
user1 = User("Alan")
```

That one-liner create a user oject. You can see we use the class name `User` to specify which class we want an instance of.

> User class -> common code and data across all users
>
> User object instances -> represent specific users

This line of code creates the object, then initialises it by calling the `__init__` constructor method. The user name "Alan" is passed as an argument. The constructor initialises the `_name` field to the value "Alan". So this user object represents a user called Alan.

Nice chap that Alan, so I hear.

The constructor code finishes executing. An _object reference_ is returned. This is how we access our object in future, so we store it in a variable `user1`.

### Call a method

We have an object instance - what next? We can call _methods_ on the object.

Methods are fancy functions at heart. The difference is a method 'knows' about the methods and data inside that object instance, without having all that information passed in as arguments.

Let's call the `greet()` method on our `user1` object:

```python
user1.greet()
```

We see this output:

```text
Welcome to Data Engineering, Alan
```

Notice how we _did not_ pass the name "Alan" in to the `greet` method. _It already knows!_.

We can create a second user object for Belisa, and greet her:

```python
user2 = User("Belisa")
user2.greet()
```

showing as output

```text
Welcome to Data Engineering, Belisa
```

This second object knows about the name Belisa.

In this way, we can create objects that represent things we care about. Many things: people, places, orders, rules, alerts, policies, products, computations and much more.

## Creating a more representative object

Data Engineering frameworks contain pre-built classes to help us work with data.

Let's create our own very basic class to help us understand what the fancy frameworks are doing.

### Creating a DataSet class

Here is the code for an `DataSet` class:

```python
class DataSet:
  def __init__(self):
    self._data = list()

  def include(self, data_point):
    self._data.append(data_point)

  def sum(self):
    total = 0

    for data_point in self._data:
      total += data_point

    return total

  def mean(self):
    number_of_data_points = len(self._data)

    if number_of_data_points == 0:
      return 0

    return self.sum() / number_of_data_points
```

This class has the following behaviour:

- It represents a data set comprising zero to many numeric data points
- We create an empty data set with no data points
- `include` will include a data point into the set
- `sum` will calculate the sum of all data points in the data set
- `mean` will calculate the mean value of all data points in the data set

Review the code and satisfy yourself it can do these things.

### Using the DataSet class

Here is how the code would be used. First we create the empty set, then we include one data point, then include a second point. At each stage, we use sum() and mean():

```python
ds = DataSet()
print(ds.sum())
print(ds.mean())

ds.include(13)
print(ds.sum())
print(ds.mean())

ds.include(17)
print(ds.sum())
print(ds.mean())
```

This creates the following output:

```text
0
0
13
13.0
30
15.0
```

Notice how the include() method builds up the data points. We do not have to pass in the existing data points _as the object instance knows them already_.

### Add ability to join DataSet objects

Let's add a `join` method to the `DataSet` class.

This method will take the data points of the object we pass to it, and include them:

```python
  def join(self, other_set):
    self._data += other_set._data
```

This takes the list of data points from `other_set` and appends them all to our `self._data` list.

We can the create a new DataSet object, `ds2`:

```python
print("Joining DataSets")
ds2 = DataSet()
ds2.include(4)
ds2.include(6)
```

and `join` it to the existing DataSet using our new method:

```python
ds.join(ds2)
```

and we can run the `sum` and `mean` methods to show the effect of the new data points:

```python
print(ds.sum())
print(ds.mean())
```

showing as output

```text
40
10.0
```

Which are the correct values.

### Objects are Abstractions

Notice in the above code that we are not dragging along lists and passing them into functions.

We can work with `DataSet` objects treating them as a whole unit - an abstraction of a set of data points.

We work at a _higher level_ closer to the problem space. Our code is descriptive: we `include()` a data point. then we find the `sum()` of all points in the set and the `mean()`. We can take two DataSet objects and `join()` them, without ever directly accessing the underlying Python list.

Not accessing the underlying list is called _encapsulation_. As if we encapsulated the code inside the class in a thick, opaque plastic resin. Exposing only the behaviours - include, sum, mean, join - that _our application_ needs is called _abstraction_.

We can see how this boosts our productivity. It also captures efforts coding so we can reuse that code instead of rewriting it ourselves.

This leads to libraries of code.

### Class DataFrame in PySpark

As an example of taking our `DataSet` idea further, consider the `DataFrame` class in PySpark.

It represents columnar data. It provides methods to read that data in from different formats. It has aggregate functions to find mean values, and much more.

It forms a highly useful toolkit for working with tabular data.

We will learn more about DataFrames in Apache Spark training.

Take a sneak peak at the [PySpark DataFrame docs](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html) to see how a simple class like our `Dataset` can be built upon.

# Next

[Working with Libraries](/07-libraries.md)

[Back to Contents](/contents.md)
