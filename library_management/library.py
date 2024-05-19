class Library:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.books = []
        self.readers = set()

    def add_book(self, book):
        self.books.append(book)

    def delete_all_copies_of_book(self, book_to_remove):
        """Remove all copies of book from library"""
        remaining_books = []
        for book in self.books:
            if book_to_remove != book:
                remaining_books.append(book)

        self.books = remaining_books

        # self.books = [book for book in self.books if book != book_to_remove]

    def display_books(self, genre=None):
        books_to_display = self.books
        if genre is not None:
            books_to_display = [book for book in self.books if book.genre == genre]
        for book in books_to_display:
            print(book)
        # OR
        # for book in self.books:
        #     if genre is None:
        #         print(book)
        #     if genre is not None:
        #         if book.genre == genre:
        #             print(book)

    def subscribe_reader(self, reader):
        self.readers.add(reader)

    def unsubscribe_reader(self, reader):
        self.readers.discard(reader)

    def lend_book(self, book, reader):
        if reader not in self.readers:
            print(f"Reader {reader} not registered. Cannot give a book out.")
            return
        if reader.n_books_from_library(self.library_id) > 3:
            print(f"Reader {reader} has taken out too many books")
            return
        if book not in self.books:
            print(f"{book} is unavailable.")
            return
        reader.take_book_out(book, self)
        self.books.remove(book)

    def return_book(self, book, reader):
        if reader not in self.readers:
            print(f"Reader {reader} not registered. Cannot give a book out.")
            return
        if reader.n_books_from_library(self.library_id) <= 0:
            print(f"Reader {reader} has no outstanding lent books.")
            return
        is_returned = reader.return_book(book, self)
        if is_returned is False:
            print(f"{book} is not from this library. You cannot return it.")
            return

        self.books.append(book)

    def list_books_lent_to_reader(self, reader):
        if reader not in self.readers:
            print(f"Reader {reader} not registered.")
            return
        return reader.list_books_lent_to_reader(self)
