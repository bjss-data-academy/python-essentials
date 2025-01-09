# Week 1 Outline

Familiarise with just enough Python, SQL and Data Engineering concepts for week 2

## Data Engineering Starter

Introducing the main ideas of Analysis, Tools, Medallion Architecture and Star Schema

May or may not do labs; may simply leave this as an explainer. Maybe exercise to draw medallion and a start schema?

- Intro to Big Data
  - Importance due to web, IoT
  - OLTP – applications
    - Easy to provide service
  - OLAP – analytics
    - Easy to analyse service
    - Batch
    - Real time
- Business Insights
  - Examples
  - Time periods: What happened when?
  - Aggregation: How much overall?
- Managing big data is hard
  - Example numbers
  - Usable queries need to be fast
  - Overview of tools
    - Apache Spark
    - Databricks
    - Azure cloud
- Medallion Architecture
  - Transforming raw data to insight
  - Bronze – Silver – Gold
  - Ingest – Add value – Present
  - Introduce Spark DataFrame object – abstraction of column data
  - ??? Lab read a CSV and display
  - ??? Lab read a JSON and display
- Star Schema
  - Invented 1990s Ralph Kimball
  - Example schema
    - See ERD in Five minutes Primer link (prerequisite)
  - Facts
    - Describe / Definition (measurement)
    - Examples of facts in typical business
  - Dimensions
    - Describe / Define
    - Examples of Dimensions
      - Date and date ranges (buckets) in particular
  - Slowly changing dimensions
    - Describe
    - Kimball Types
    - Example Type 0
    - Example Type 1
    - ??? Type 2
  - Walk through example of a complete Star Schema ERD
- Enforced Fun Quiz
- Further Reading
  - Ralph Kimball site

## Python Essentials

Basics of Python language and built-in data types that will be used during Spark programming. Labs throughout.

- Install Python (or use Notebook??)
- Hello, Big Data
- Variables
  - Built-in primitive types
  - Dynamic typing
- String manipulation
  - F strings
  - Operations on strings <https://www.w3schools.com/python/python_strings.asp>
- Working with dates
- If – else – elif
  - Whitespace defines code blocks
- Loops
- Variable scope
- Functions
  - Overview
  - Calling a function: print (“hello”)
    - Arguments – values we call with
    - Returns
    - Type hints
  - Defining a function
    - Signature
      - Name – name what it does
      - Parameters – name given to arguments in body
      - Code block
      - Return value
    - Example function with multiple calls
  - Lambda
- Data structures
  - Tuple
  - List
    - Iteration
    - CRUD operations
    - List comprehension
      - Filtering
      - Using lambda syntax
      - Sorting
  - Dictionary
    - CRUD operations
    - Lookup usage
  - Set
- Functional Programming ideas
  - Why FP is useful for Data Engineering
  - Pure functions
  - Immutable data – create new, not modify old
  - First class functions
    - functions references in variables
    - Functions passed to functions
- Object basics
  - Explain data + methods bundled together
  - String object
    - upper()
    - split()
  - Pyspark DataFrame object
    - Overview
    - Some methods
    - Some examples
- Libraries
  - What they are and why useful
  - Import statement
  - Using an imported function / class
- Further Reading
  - BJSS Academy FP Python
  - W3Schools Python
- Labs – define exercises, provide solutions

## Intermediate SQL

Prerequisite: BJSS Academy SQL fundamentals. Install Postgress and code aloing using psql. Github a population script with example data

- Refresher
  - Table, row, column
  - Primary Key
    - Composite key – business values
    - Surrogate Key – unique row ID unrelated to business
  - Foreign Keys
  - SELECT columns from single table WHERE
  - ORDER BY
  - Inner Join on two tables
  - 1:1 relations
  - 1:many relation
  - Many:many relation – join table or link table
- Aggregates
  - Important in analysis – explain why
  - COUNT
  - DISTINCT
  - SUM
  - AVG
  - ??? Any others?
- GROUP BY
- HAVING
- Joining multiple tables
- Left join
  - Uses in analytics
  - NULLs and their meaning
- Other joins – join diagram
- Subselects
  - Select on a select
  - Views
- Window functions
- Further Reading
  - Sqlbolt

## Apache Spark Basics

- Todo
- Maybe just start week 2
