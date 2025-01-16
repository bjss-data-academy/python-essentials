# Libraries

Once we have defined functions and classes, we can use them as building blocks for a bigger program.

A _Library_ is a pre-written collection of these definitions. We pull in the library, and start using the functions and classes it provides.

Python is the premier language for Data Engineering because it has the widest range of helpful libraries.

## Creating a library

Remember our `DataSet` class we made? Let's turn that into a reusable library.

Create a file `dataset.py` and paste in our `DataSet` class:

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

  def join(self, other_set):
    self._data += other_set._data
```

No changes to the `DataSet` class code are necessary. We simply need to move it into a file we can use as a library.

The name of the file (without .py extension) will be the name of the library.

Code is at [src/dataset.py](/src/dataset.py)

## Using the library

Python supports this with the `from ... import` statement:

```python
from dataset import DataSet

ds = DataSet()
ds.include(1)
ds.include(2)
ds.include(3)

print(ds.sum())
print(ds.mean())
```

Notice the `from ... import` statement in the first line. This tells Python to pull in the `DataSet` class from the `dataset` library, and make it available for use in our program. It is just as if we had written it ourselves.

The next part of the Python code makes use of the `DataSet` class. Nothing special - we have just saved ourselves the effort of designing, writing, testing and maintaining a `DataSet` component. We can easily share this around the team, or even the wider world.

Code is at [src/libraries.py](/src/libraries.py)

## Import statement

Python supports an alternative syntax, using `import':

```python
import dataset

ds = dataset.DataSet()
ds.include(1)
print(ds.sum())
```

Here, every component of the library is imported. But note we must use the _namespace_ of the library name to access `DataSet`:

```python
ds = dataset.DataSet()
```

This helps avoid naming conflicts when importing multiple libraries.

## Useful Python libraries for Data Engineering

- [NumPy](https://numpy.org/) Scientific/Numerical computing
- [Pandas](https://pandas.pydata.org/) Data Analysis
- [Pyspark](https://spark.apache.org/docs/latest/api/python/index.html) Apache Spark data tools
- [BeautifulSoup](https://spark.apache.org/docs/latest/api/python/index.html) Web Scraper

There is a serious amount of data firepower in those four libraries alone.

# Next

[Unit Testing](/08-unit-test.md)

[Back to Contents](/contents.md)
