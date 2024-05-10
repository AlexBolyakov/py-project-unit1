### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["J.B. Peterson", "C. Newport", "N.V. Gogol", "I.V. Turgenev", "F.M. Dostoevsky", "L.N. Tolstoy", "A.S. Pushkin"]
print("my authors:", my_authors)
# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here

my_authors.append("M.V. Lomonosov")
print("my authors_append: ", my_authors)

# Example: my_authors.append("H.G. Wells")
my_authors.pop(1)
print("my authors_pop: ", my_authors)

# Now let's remove an element in the list


# Code here
my_authors.remove("I.V. Turgenev")
print("my authors_remove: ", my_authors)

# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here

print("my authors_element[1] ", my_authors[1])


# Example: my_authors[2]


# Now slice the list.

# Code here
# Example: my_authors[1:4]

print("my authors_slice[2:]: ", my_authors[2:])



### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here

my_author_tuple = ("John Steinbeck", "Lisa Alther", "P. Auster", "Issac Asimov", "Willa Cather", "Saul Bellow")
print("my authors_tuple: ", my_author_tuple)
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

# Code here

my_author_set = {"John Steinbeck", "Lisa Alther", "P. Auster", "Issac Asimov", "Willa Cather", "Saul Bellow"}
print("my authors_set: ", my_author_set)

# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

# Code here

my_author_set.add("Walter Abish")
print("my authors_set_add: ", my_author_set)

# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

# Code here

my_author_set.add("Walter Abish")
print("my authors_set_add again: ", my_author_set)

# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here

for author in my_authors:
    print(author)

for item in my_author_set:
    print(item)

for element in my_author_tuple:
    print(element)



# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

