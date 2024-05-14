class User:
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.borrowed_books = [] # stores book objects 