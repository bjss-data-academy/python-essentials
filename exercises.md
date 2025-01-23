# Python Exercises

Let's apply what we've learned.

## Task 1 Test existing `DataSet` code

Write unit tests for our [`DataSet`](/src/dataset.py) class.

- Aim for 100% coverage. There is simply no reason not to for this.
- Cover happy paths (expected behaviours for core use cases)
- What error paths should we test?
- Are there any boundary conditions to test? (example: empty dataset)

## Task 2 Test-drive new `DataSet` features

Have a go at writing tests first as you add these features to `DataSet`:

- median() returns the [median](https://en.wikipedia.org/wiki/Median) value of the set
- mode() returns the [mode](<https://en.wikipedia.org/wiki/Mode_(statistics)>) of the set
- max() returns the highest number
- min() returns the lowest number
- range() returns a tuple of (min, max)
- window(min, max) returns how many values lie within (min, max) bounds

## Task 3 Read CSV files

- Create a class `DataSetReaderCsv' with a `parse(file)`method that returns a`DataSet`
- This will need a unit test that is really a component test: it will need to access the file system. we will need files that allow us to test a range of possible inputs to our reader.

## Task 4 scrape a web page

- Create a class `DataSetReaderWeb` with a `parse(url)`method that returns a`DataSet`
- Use the [beautiful soup](https://pypi.org/project/beautifulsoup4/) library to parse html and extract the numbers to include in a DataSet object
- Use this web page: http://cyan-ali-20.tiiny.site as source (html from [src/test-results.html](src/test-results.html)
- This will need a unit test that is really a component test: it will need to access the web.
  -- What sort of problems might we encounter when tests access the web?

# Next

[Further reading](/further.md)

[Back to Contents](/contents.md)
