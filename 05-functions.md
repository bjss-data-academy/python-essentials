# Functions and Functional Programming

So far, our Python code has been one, giant 'shopping list' of instructions. That's fine for tiny scripts, but professional code needs better organisation.

Fortunately, Python provides ways to organise our code. The simplest is a function.

Code for this section is at [src/functions.py](/src/functions.py)

## Python functions

A function is a reusable block of code that is given a name, supplied with some data to work with and returns a result.

### Defining a function

Here is a function we've decided to name `double_value`. This name describes what the function does: it takes the value we give it and returns double that value.

```python
# function definition
def double_value( original ):
    doubled = original + original
    return doubled
```

Let's break this down:

- `def` keyword says we are starting a function definition
- `double_value` - that's the name of the function. We choose that
- `original` - this is the name of our one and only parameter to our function
- `return` - this keyword will exit the function and pass back a value, here `doubled`

So far, this code only defines that a function `double_value` exists. It does not execute the code in the definition. To make that happen, we must call the function.

### Calling a function

We use the name of our function, supply the necessary parameter values (called _arguments_) and store away any return value.

To call our `double_value` function, we write:

```python
result = double_value(3)
print(result)
```

We pass in the argument 3. The code inside the function definition now executes, with parameter `original` taking on the argument value of 3. The function code block runs, and returns 6. We store that away in variable result.

#### A note on data types

You'll notice that our function definition says nothing about what data type we can pass to the function, nor what to expect as a return.

This is because Python is a dynamically typed language.

Above, we called the function with the integer value 3. But what if we called it with the string `weird?`.

```python
print ( double_value("weird?") )
```

It generates the output

```text
weird?weird?
```

That happened because Python decides that `original` is a string type. The function's code block then resolves the + operator to the string concatenation operation. It's probably not what we wanted at all.

This is generally speaking a very bad idea, leading to some very difficult to spot bugs.

To help avoid such accidental misuse, we can use Python [type hints](https://docs.python.org/3/library/typing.html), [unit tests](/08-unit-test.md) and generally design our code to avoid such a problem.

We'll cover unit tests a little later, as they are really important in engineering.

### Advice on functions

Python functions follow the same general advice as every other language:

- Name them for what they do
- Name parameters for what information they hold
- Give them one reason to change
- Use them to create useful abstractions

## Lambda functions

Python has a short form for one-line functions which can be useful:

```python
say_hello = lambda name: "Hello, " + name + "!"
print(say_hello("Alan"))
```

These are useful to pass into other unfctions as arguments. Common use cases include filter predicates and sort comparisons.

## Functional Programming ideas

Python offers some support for the Functional Programming paradigm. This is very useful in Data Engineering.

An FP program organises code around transforms applied to a flow of data. Transforms are coded as functions/lambda. Data flows often use Python built-in structures, such as tuples and lists.

There are a few big ideas behind functional programming.

### Pure functions

A function should produce a return based _only_ on the arguments supplied to it. It should not involve any global data. Global data includes global variables, hard-coded calls to other functions that generate data, random generators, third-party web services and more. These things can be used, but must be pushed out of the pure function into the calling context.

Pure functions are repeatable and predictable: what you get depends only on what you put in. As a reult, testing pure functions is simple.

The previous examples are pure functions.

### Immutability

A pure function will not change any of its input data. Instead, it will return fresh data.

This code will add a book to a list of books, but it does so by modifying the original list:

```python
def add_book_mutating( books, new_book):
    books.append(new_book)

books = ["Java OOP Done Right", "Tom the Racer", "Frankenstein"]
add_book_mutating(books, "Magnets, Bulbs and Batteries")

## Note the input parameter books has been changed!
print(books)
```

While this may be useful, it goes against the FP rule of a repeatable, pure function. if we called it multiple times, we would get multiple copies of the new book added (try it!).

Instead, FP requires that pure functions leave the original input data unchanged:

```python
def add_book( books, new_book):
    new_books = books.copy()
    new_books.append(new_book)
    return new_books

books = ["Java OOP Done Right", "Tom the Racer", "Frankenstein"]
updated_books = add_book(books, "Magnets, Bulbs and Batteries")

## Input parameter books has NOT been changed!
print("original books", books)
print("updated books", updated_books)
```

The key technique here is to make a _copy_ of the parameter `books` we passed in. This create a new working variable for our output, preserving the original.

## First-order functions

Python functions are first-order, meaning that they are treated exactly as any other data type.

This has a number of advantages:

- We can hold a reference to a function
- We can pass a function into another function as an argument

Here's an example. We will write a function to remove a book from a list of books. To make it flexible, we will pass in a deciding function (termed a _predicate_) that decides whether the book should be removed.

```python
def remove_books( books, should_remove):
    new_books = list()

    for book in books:
        if not should_remove(book):
            new_books.append(book)

    return new_books
```

Notice how the parameter `should_remove` is _called_ as a function, with a single argument of the book title passed into it. It is expected that it will return true or false. This is often known as a _callback_ function, as we 'call back' to that function from inside our code.

To call `remove_books`, we need to supply a list of books to remove from, and a suitable callback function.

Let's remove books whose title is a single word only. We'll determine that by passing in a callback function that checks if the suppled book name has any spaces or not:

```python
books = ["Java OOP Done Right", "Tom the Racer", "Frankenstein"]

is_single_word = lambda title: not ' ' in title
without_single_word_titles = remove_books(books, is_single_word)
print("removed single word titles", without_single_word_titles)
```

Our callback is defined as a lambda `is_single_word` and passed in to `remove_books`

To illustrate the flexibility this brings, let's call the same `remove_books` function, but this time passing in a different callback. This time, we will remove books containing the word 'Java' in their title (much as it pains me to say that):

````python
books = ["Java OOP Done Right", "Tom the Racer", "Frankenstein"]

is_about_java = lambda title: 'Java' in title
without_java = remove_books(books, is_about_java)
print("Java banned", without_java)```
````

We get a different result.

Note how the function `remove_books` has not changed in any way, yet has been made to behave differently.

This is an example of the Open-Closed Principle (OCP) at work - a function is open for extension (new behaviour), but closed against modification (code change). OCP is one of the five SOLID principles that help us design sane software.

First-order functions are very useful for creating plug-and-play building blocks that transform data, yet can be configured without hacking away at the code.

As a final mind-bending example, lets supply a list of callbacks to our function:

```python
def remove_books_multi_filter( books, book_filters):
    new_books = books.copy()

    for book_filter in book_filters:
        new_books = remove_books(new_books, book_filter)

    return new_books
```

We can call this with our previous lambdas:

```python
is_single_word = lambda title: not ' ' in title
is_about_java = lambda title: 'Java' in title

book_filters = [is_single_word, is_about_java]
remaining_books = remove_books_multi_filter(books, book_filters)
print("All filters applied", remaining_books)
```

After running this code, we're left with only the book "Tom the Racer".

This is a very powerful approach to composing functions in a Functional Programming paradigm.

FP is not the only game in town. Let's look at another important programming paradigm - _object oriented programming_.

# Next

[Object Orientation basics](/06-objects.md)

[Back to contents](/contents.md)
