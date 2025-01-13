# Making decisions with conditionals

Python supports keywords `if`, `else` and `elif` so that we can make decisions with conditional code.

## Basic if-else example

A basic example is:

```python
favourite_food = "curry"
print ("Your favourite food is", favourite_food)

if favourite_food == "curry":
    print("You have great taste")
else:
    print("You really should try curry")
```

You can run the code in [src/conditionals.py](src/conditionals.py)

## If has a conditional expression

The if keyword is followed by a _conditional expression_. These expressions must evaluate to eith er TRUE or FALSE.

In the example, the condition is "does the value of the `favourite_food` variable equal `'curry'`". When this is true, the _code block_ linked to the true branch will run.

The code block contains the single line `print("You have great taste")` in this case.

There are no parenthesis required around the conditional expression.

## Python uses whitespace for code blocks

Love it or hate it, Python uses whitespace to mark out code blocks. Other languages from the C family use curly braces {}, yet others use BEGIN...END.

But not Python.

Python takes the, er, creative choice that code blocks will be marked out by the indentation level of the source code. We can see that the code block under the if statement is indented.

For multi-line code blocks, every line must start with the same indentation.

You can argue yourselves over whether it should be tabs or spaces ;)

## Else introduces an alternate code path

In the example above, what happens when the if condition is false?

Two things:

- The if code block does NOT run
- The else code block does run

## Else is optional

Else is optional. If you don't have any code to run for else, don't add the else block. It only adds clutter.

## Elif supports if - else - if chains

Python has the `elif` keyword which is a contraction of `else if`. This has the advantage that it allows complex conditional sequences to be built up. It also has the considerable disadvantage that it allows complex conditional sequences to emerge like a festering sore.

Here's `if`, `elif` and `else` in action:

```python
fruit = "banana"
pet = "dog"

if fruit == "banana":
    print("You like bananas - and that's all that matters")
elif pet == "cat":
    print("You don't like bananas, but do like cats. That's alright then.")
else:
    print("Don't like bananas, don't like cats. You monster")
```

See if you can figure out what gets printed for the combinations:

- banana, dog
- apple, cat
- apple, hamster

Use with caution. Avoid where possible.

## Logical operators in conditional expressions

Keyword 'elif' provides a way to make complex sequences of conditional logic. It's not always the right tool for the job.

Suppose we want to run some code where more than one condition is true:

```python
fruit = "grape"
snack = "cheese"

if fruit == "grape" and snack == "cheese":
    print("Grapes and cheese! A cheeseboard - what a splendid idea!")
else:
    print("I'd send that cheeseboard back if I were you")
```

The if code block runs when both conditions are true, due to that `and` operator. The whole is true only if the first part AND the second part are true,

There are other useful logical operators you can use. Common ones include _or_ and _not_.

You can use many sub expressions joined by combinations of and, or and not. Yes, that does get as convoluted and hard to work with as it sounds.

Once we've covered functions, you'll be able to untangle such complex conditional expressions with ease.

# Next

[Repeating tasks with loops](/03-loops.md)

[Back to contents](/contents.md)
