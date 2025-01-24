# Repeating tasks with loops

Loops are very handy for repetitive tasks where we need to run a code block many times. Python supports a number of forms, all based around the `for` keyword.

## For loops

If we want to loop a fixed number of times, we use the`for...range` loop:

```python
for count in range (3):
    print( "Repeat number", count )

```

You can run this code in [/src/loops.py](/src/loops.py)

Note:

- `for` keyword
- code block is indented
- range(n) will iterate through integers 0...n-1

We can use two arguments in range, a lower and "one more than upper" bound:

```python
for count in range(1,6):
    print("Counting between 1 aand 5 inclusive", count)
```

Python uses the `for` keyword for iterating over lists and for things called _list comprehensions_. We'll return to these handy things, once we look at lists, a little later on.

## While loops

Python supports `while` loops which are very general purpose.

Here is a simple while loop example. It echoes back whatever you type, until you type the word _quit_:

```python
word = input ("Type a word, or type 'quit' to end: ")

while word != "quit":
    print("you typed", word)
    word = input ("Type a word, or type 'quit' to end: ")
```

### `break` and `continue` keywords

The `continue` keyword is used to skip a block of code inside a loop, and go on to execute the next run of that loop.

Here, we avoid printing out the number 4, by using `continue` to skip the printing:

```python
for i in range(6):
    if i == 4:
        continue

    print(i)
```

A similar keyword `break` exists. This will exit the loop without completing any further iterations:

```python
for i in range(666):
    if i == 4:
        break

    print("break", i)

print("break took us out of the loop without completing it")
```

Both `break` and `continue` are best avoided as they complicate control flow. We can generally find a way to do the same job without them.

# Next

[Built-in data structures](04-data-structures.md)

[Back to contents](/contents.md)
