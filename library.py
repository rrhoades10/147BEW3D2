from book import Book
from user import User

class Library:

    def __init__(self):
        self.books = {} #this could also be a list of objects
        self.current_loans = {}
        # self.users = [] if you wanted to store users in your library

# library is going to be a dictionary within a main() (run) function
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter isbn: ")
        # key is the isbn -> value is a Book object
        book = Book(title, author, isbn)
        self.books[isbn] = book

    def checkout_book(self):
        isbn = input("Enter the ISBN of the book to borrow: ")
        user = input("Enter the user name: ")
        library_id = input("What is the users id?")

        user = User(user, library_id) #creates a user object
        # checking that the isbn is a current key in our self.books dictionary

        if isbn in self.books and self.books[isbn].borrow_book():
            self.current_loans[isbn] = user #adding the user object as the value
            # adding the book to the user attribute borrowed_books
            user.borrowed_books.append(self.books[isbn])
            # accesing the book object (which is a value) associated with the isbn key
            # im calling the get_title() method from the book object stored in my dictionary at the key of
            # whatever the isbn is
            print(f"Book {self.books[isbn].get_title()} checked out to {user}")
        else:
            print("That book is unavailable")

    def checkin_book(self):
        isbn = input("Enter ISBN of the book to return: ")
        if isbn in self.books and isbn in self.current_loans:
            self.books[isbn].return_book()
            del self.current_loans[isbn]
            print(f"Book {self.books[isbn].get_title()} was returned")








