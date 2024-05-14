# Library Management System

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True
        

    # Getters and Setters for the above attributes
    def get_title(self):
        return self.__title
    
    def is_available(self):
        return self.__is_available
    
    def get_isbn(self):
        return self.__isbn
    
    def get_author(self):
        return self.__author

    def set_is_available(self, availability):
        self.__is_available = availability

    def borrow_book(self):
        # calling the getter to check if self.__is_available is True
        if self.is_available():
            # calls the setter to change availability to False because the book has been checked out
            self.set_is_available(False)
            
            return True
        return False
    
    def return_book(self):
        self.set_is_available(True)
        # self.__is_available = True










    
    

    




