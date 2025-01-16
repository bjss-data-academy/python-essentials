# Python Unit Testing

## Testing code

We may get a kick from having code that compiles, but users find it jolly nice to have code that _actually works_.

Hands up everyone who normally writes code and thinks 'that will never work, because I wrote it'?

_I see all those hands down_. We are nothing if not a confident bunch, we engineers.

Traditional engineering has always focussed on _validation_ of components.

If our bridge claims it can support a weight of one tonne, let's validate that claim. The test is to put one tonne on the bridge and see what happens. It will pass or fail.

Validating software components is the same thing. We call a component a _unit_ and the validation process a _test_. So in software, we do _unit testing_.

## Testing by hand

Let's say we've written a function that returns the sum of a list of numbers - [src/sum.py](/src/sum.py)

How would we test it?

Here's the standard approach:

- Pick a set of numbers as input: say 1, 2 and 3
- Run the code with those numbers
- Check that the code gives the expected answer of 1 + 2 + 3 = 6

To do this by hand, we would write a simple test script that printed the result:

```python
input = [1, 2, 3]
actual = calculate_sum( input )
print( "input", input, "actual", actual )
```

Run the script, and eyeball the printout:

```text
input [1,2,3] actual -372.6
```

_Oh dear_, or engineering phraseology to that effect.

At least we found out our code was wrong _now_, and not in production from an irritable user.

We fix our bug and run the test again. Once we see the expected value has been output, we know our code works as expected.

## Regression testing

One problem with our shiny new working code is that it will be changed. We work in teams. We work on long running projects. We work using agile methods - we expect change.

It is possible (likely, even) that a future change will _break_ our code.

To detect this, we like to run every test that we ever ran on every change.

This is _regression testing_. We do not want our code to regress and become less than it was.

_Does this sound like a giant nuisance to you?_

Me too. There must be a better way.

If only there were some way for a computer programmer to automate repetitive tasks?

## Automated testing

_Code_. Of course, code is the answer when you are a programmer.

We can automate our three test steps that we did by hand. Let's modify our previous script:

```python
# Arrange
input = [1, 2, 3]

# Act
actual = calculate_sum( input )

# Assert
expected = 1 + 2 + 3
if actual == expected:
    print( "pass")
else:
    print("test failed")
```

Notice how the checking is done using an if statement - it has been automated. the rest is the same. We picked some numbers, ran our function, and figured out what to expect when it works.

### Arrange, Act, Assert

Also notice the comments, splitting that test into three sections Arrange, Act, Assert (AAA).

These are the three steps we started with:

- Arrange: Pick some test input
- Act: Run our code that we are testing
- Assert: Automatically verify that we got the right answer

### Some problems with our script

You can probably spot a few problems with that basic script:

- Adding tests is hard; we will get variable collisions
- What are we testing? It doesn't say
- Output is pass or fail, but what passed? what failed?
- How do we get a simple "All PASS, good to go"

We will solve these problems with a _unit testing library_ called `pytest`.

## Automated testing with pytest

Pytest enables us to write tests as separate, well-named functions. We can include details about test failures. We can get a simple report at the end of a test run.

### Install Pytest

First install pytest. The easiest way is using `pip`:

```text
pip install -U pytest
```

and check it installed using

```text
pytest --version
```

If that didn't work, refer to the [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html) docs for help.

### Creating a unit test with pytest

We can take our existing script and modify it.

Create a file called `test_sum.py` and inside, create this function:

```python
from sum import calculate_sum

def test_sums_three_numbers():
        # Arrange
    input = [1, 2, 3]

    # Act
    actual = calculate_sum( input )

    # Assert
    expected = 1 + 2 + 3
    assert actual == expected
```

_Note:_ code at [src/test-sum.py](/src/test_sum.py) and [src/sum.py](/src/sum.py)

We've replaced the if-else with the `assert` keyword. Pytest will collect all the results of `assert` statements and summarise them into a report.

### Running unit tests

We can run all tests from the command line by navigating to the directoy containing our test files, and running:

```text
pytest
```

In our case, we get the following output:

![Test passing in pytest](/images/pytest-pass.png)

Our code has been run, validated against an expected outcome, and we have done this automatically.

> Notice how quick that was

## TDD: Using tests before code to specify a design

You'll notice that our test says nothing at all about how the function is implemented inside. This is important.

> Test observable behaviour, not implementation detail

This leads us to another observation: tests are _executable specificications_. They are requirements as code.

We can write tests first - before we write the code under test - and use it to capture:

- The behaviour of the code
- The programming interface the rest of the code will use

This is closer to specification and design than to coding, and as such is very useful in irganising code to have clear boundaries.

For much more on this approach, have a look at our Academy guide to [Advanced TDD](https://github.com/bjssacademy/advanced-tdd)

# Next

[Further reading](/further.md)

[Back to Contents](/contents.md)
