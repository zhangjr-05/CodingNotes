class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    

class Reader:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False
    
class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def find_reader_by_id(self, reader_id):
        for reader in self.readers:
            if reader.id == reader_id:
                return reader
        return None
    

library = Library()
book1 = Book("查理九世", "雷欧幻像")
reader1 = Reader("张三", "001")

library.add_book(book1)
library.add_reader(reader1)

