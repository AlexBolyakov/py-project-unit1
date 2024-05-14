### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

# def main_menu():
    
#     while True:
#         print("\nMain Menu:")
#         print("1. Add a book")
#         print("2. Show all books")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_book()
#         elif choice == "2":
#             show_all_books()
#         elif choice == "3":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please enter a number from 1 to 3.")

# def add_book():
#     title = input("Type the title of the book to add: ")
#     if title == "":
#         title = input("It cannot be an empty string, please type it again: ")

#     author = input("Enter the author of the book: ")
#     if author == "":
#         author = str(input("It cannot be an empty string, please type it again: "))

#     try:
#         year = int(input("What year was this book published? "))
#     except ValueError:
#         year = int(input("Type the year of the book to add: "))
#     try:
#         rating = float(input("What was the rating of the book? "))
#     except ValueError:
#         rating = float(input("Type the rating of the book to add: "))
#     try:
#         pages = int(input("What was the total number of pages in the book? "))
#     except ValueError:
#         pages = int(input("Type the number of pages in the book: "))

    
    
#     book_info = f"{title}, {author}, {year}, {rating}, {pages}\n"

#     with open("library.txt", "a") as f:
#         f.write(book_info)


#     print(f"A new book was added:\n Title: {title}\n Author: {author}\n Year: {year}\n Rating: {rating}\n Pages: {pages}\n")
#     return book_info

# def show_all_books():
#     print("\nList of Books:")
    
#     with open("library.txt", "r") as f:
#         books = f.readlines()
        
#         for book in books:
#             title, author, year, rating, pages = book.split(", ")
#             print({
#             "title": title,
#             "author": author,
#             "year": int(year),
#             "rating": float(rating),
#             "pages": int(pages)
#         })
        
# main_menu()


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def main_menu():
    
    while True:
        print("\nMain Menu:")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Display total number of the pages in the library")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            show_all_pages()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def add_book():
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

    
    
    book_info = f"{title}, {author}, {year}, {rating}, {pages}\n"

    with open("library.txt", "a") as f:
        f.write(book_info)


    print(f"A new book was added:\n Title: {title}\n Author: {author}\n Year: {year}\n Rating: {rating}\n Pages: {pages}\n")
    return book_info

def show_all_books():
    print("\nList of Books:")
    
    with open("library.txt", "r") as f:
        books = f.readlines()
        
        for book in books:
            title, author, year, rating, pages = book.split(", ")
            print({
            "title": title,
            "author": author,
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages)
        })

def show_all_pages():
    total_pages = 0
    with open("library.txt", "r") as f:
        books = f.readlines()
        
        for book in books:
          title, author, year, rating, pages = book.strip().split(", ")
          total_pages += int(pages)

    print("Total pages from all books:", total_pages)
    return total_pages

   
            


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

if __name__ == "__main__":
    main_menu()

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

