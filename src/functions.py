# function definition
def double_value( original ):
    doubled = original + original
    return doubled

# function call
result = double_value(3)
print(result)

# Probably unexpected behaviour with strings ...
print ( double_value("weird?") )

# Lambda

say_hello = lambda name: "Hello, " + name + "!"
print(say_hello("Alan"))

# Not immutable
def add_book_mutating( books, new_book):
    books.append(new_book)

books = ["Java OOP Done Right, Tom the Racer"]
add_book_mutating(books, "Magnets, Bulbs and Batteries")

## Note the input parmeter books has been changed!
print(books)

# Immutable
def add_book( books, new_book):
    new_books = books.copy()
    new_books.append(new_book)
    return new_books

books = ["Java OOP Done Right", "Tom the Racer", "Frankenstein"]
updated_books = add_book(books, "Magnets, Bulbs and Batteries")

## Note the input parmeter books has been changed!
print("original books", books)
print("updated books", updated_books)

# Book filter with predicate
def remove_books( books, should_remove):
    new_books = list()

    for book in books:
        if not should_remove(book):
            new_books.append(book)
    
    return new_books

books = ["Java OOP Done Right", "Tom the Racer", "Frankenstein"]

is_single_word = lambda title: not ' ' in title
without_single_word_titles = remove_books(books, is_single_word)
print("removed single word titles", without_single_word_titles)

is_about_java = lambda title: 'Java' in title
without_java = remove_books(books, is_about_java)
print("Java banned", without_java)

# Multi filter version - list of callbacks
def remove_books_multi_filter( books, book_filters):
    new_books = books.copy()

    for book_filter in book_filters:
        new_books = remove_books(new_books, book_filter)

    return new_books

is_single_word = lambda title: not ' ' in title
is_about_java = lambda title: 'Java' in title

book_filters = [is_single_word, is_about_java]
remaining_books = remove_books_multi_filter(books, book_filters)
print("All filters applied", remaining_books)
