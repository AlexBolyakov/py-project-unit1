my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_books = [{
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374},

    {"title": "12 Rules for life",
    "author": "Jordan Peterson",
    "year": 2012,
    "rating": 4.83,
    "pages": 350

    }]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def my_book_info(my_book):
    '''message'''
    book = f"Here is the information about the book: {my_book}"
    return book
  
print(my_book_info(my_book))  

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

# The function below returns the title of the book

def my_book_title(my_book):
    title = f"The title of the book: {my_book["title"]}"
    return title

print(my_book_title(my_book))

# The function below returns the author of the book

def my_book_author(my_book):
    author = f"The authour of the book is {my_book["author"]}"
    return author
print(my_book_author(my_book))

# The function below returns the year of the book

def my_book_year(my_book):
    year = f"The year of the book is {my_book["year"]}"
    return year

print(my_book_year(my_book))

# The function below returns rating of the book

def my_book_rating(my_book):
    rating = f"The rating of the book is {my_book["rating"]}"
    return rating

print(my_book_rating(my_book))

# The function below returns the total number of pages in the book

def my_book_pages(my_book):
    pages = f"Total number of pages is {my_book["pages"]}"
    return pages

print(my_book_pages(my_book))



# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

