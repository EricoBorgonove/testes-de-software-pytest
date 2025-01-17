# library.py
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)
        return f"'{book_title}' added to the library"

    def find_book(self, book_title):
        return book_title in self.books
