### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():

#     title = input("Type the title of the book to add: ")
#     author = input("Enter the authour of the book to add: ")
#     year = input("Type the year of the book to add: ")
#     rating = input("Type a rating of the book to add: ")
#     pages = input("What is the number of pages in the book? ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     print(book_dictionary)
#     return book_dictionary
    
# create_new_book()

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():

#     title = input("Type the title of the book to add: ")
#     author = input("Enter the authour of the book to add: ")
#     year = int(input("Type the year of the book to add: "))
#     rating = float(input("Type a rating of the book to add: "))
#     pages = int(input("Type the number of pages in the book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     print(book_dictionary)
#     return book_dictionary
    
# create_new_book()



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def create_new_book():

#     title = input("Type the title of the book to add: ")
#     author = input("Enter the authour of the book to add: ")
#     year = int(input("Type the year of the book to add: "))
#     try:
#         rating = float(input("What was a rating of the book: "))
#     except:    
#         rating = float(input("Type a rating of the book to add: "))
#     try:
#         pages = int(input("What was the total number of pages in the book? "))
#     except:    
#         pages = int(input("Type the number of pages in the book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     print(book_dictionary)
#     return book_dictionary
    
# create_new_book()

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# def main_menu():

#     my_books_list = [{
#         "title": "Then Hunger Games",
#         "author": "Suzanne Collins",
#         "year": 2008,
#         "rating": 4.32,
#         "pages": 374},

#         {"title": "12 Rules for life",
#         "author": "Jordan Peterson",
#         "year": 2012,
#         "rating": 4.83,
#         "pages": 350},
        
#         {"title": "Deep Work",
#         "author": "Cal Newport",
#         "year": 2007,
#         "rating": 4.67,
#         "pages": 467},
        
#         {"title": "Of Boys and Men",
#         "author": "Richard Reeves",
#         "year": 2022,
#         "rating": 4.51,
#         "pages": 280},

#         {"title": "The Powe of Now",
#         "author": "Eckhart Tolle",
#         "year": 1997,
#         "rating": 4.2,
#         "pages": 258}
#         ]
    
    
#     input("Welcome to Main Menu of the App! Press Return to continue.")
    
#     title = input("Type the title of the book to add: ")
#     if title == "":
#         title = input("It cannot be an empty string, please type it again: ")
    
#     author = input("Enter the author of the book: ")
#     if author == "": 
#         author = str(input("It cannot be an empty string, please type it again: "))
    
#     try:
#         year = int(input("What year was this book published? "))
#     except:
#         year = int(input("Type the year of the book to add: "))
#     try:
#         rating = float(input("What was a rating of the book: "))
#     except:    
#         rating = float(input("Type a rating of the book to add: "))
#     try:
#         pages = int(input("What was the total number of pages in the book? "))
#     except:    
#         pages = int(input("Type the number of pages in the book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     my_books_list.append(book_dictionary)
#     print(f"Successfully added book: {book_dictionary}")
#     print(f"Here is the currect list of books on file: {my_books_list}")
#     return my_books_list

# main_menu()


   

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu():
    my_books_list = [
        {
            "title": "The Hunger Games",
            "author": "Suzanne Collins",
            "year": 2008,
            "rating": 4.32,
            "pages": 374
        },
        {
            "title": "12 Rules for Life",
            "author": "Jordan Peterson",
            "year": 2012,
            "rating": 4.83,
            "pages": 350
        },
        {
            "title": "Deep Work",
            "author": "Cal Newport",
            "year": 2007,
            "rating": 4.67,
            "pages": 467
        },
        {
            "title": "Of Boys and Men",
            "author": "Richard Reeves",
            "year": 2022,
            "rating": 4.51,
            "pages": 280
        },
        {
            "title": "The Power of Now",
            "author": "Eckhart Tolle",
            "year": 1997,
            "rating": 4.2,
            "pages": 258
        }
    ]

    while True:
        print("\nMain Menu:")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            my_books_list = add_book(my_books_list)
        elif choice == "2":
            show_all_books(my_books_list)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def add_book(books_list):
    title = input("Type the title of the book to add: ")
    if title == "":
        title = input("It cannot be an empty string, please type it again: ")

    author = input("Enter the author of the book: ")
    if author == "":
        author = str(input("It cannot be an empty string, please type it again: "))

    try:
        year = int(input("What year was this book published? "))
    except ValueError:
        year = int(input("Type the year of the book to add: "))
    try:
        rating = float(input("What was the rating of the book? "))
    except ValueError:
        rating = float(input("Type the rating of the book to add: "))
    try:
        pages = int(input("What was the total number of pages in the book? "))
    except ValueError:
        pages = int(input("Type the number of pages in the book: "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    books_list.append(book_dictionary)
    print(f"Successfully added book: {book_dictionary}")
    return books_list

def show_all_books(books_list):
    print("\nList of Books:")
    for book in books_list:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Rating:", book["rating"])
        print("Pages:", book["pages"])
        print()

main_menu()
