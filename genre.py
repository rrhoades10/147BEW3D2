from book import Book
class Genre:

    def __int__(self, genre_name, genre_description):
        self.genre_name = genre_name
        self.genre_description = genre_description

scifi = Genre("SciFi", "Cool science stuff")


class FictionBook(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn, author)
        self.genre = "Fiction"
        self.description = "This stuff didnt happen but its cool"

fibook = FictionBook("LOTR", "Tolkien", "4142344")