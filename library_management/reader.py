class Reader:
    def __init__(self, name, citizen_number):
        # TODO: Validate name and citizen number
        self.name = name
        self.citizen_number = citizen_number
        self.books_lent = dict()  # {library_id: [books]}

    def take_book_out(self, book, library):
        books_taken_from_library = self.books_lent.get(library.library_id, [])
        books_taken_from_library.append(book)
        self.books_lent[library.library_id] = books_taken_from_library

    def return_book(self, book, library):
        books_taken_from_library = self.books_lent.get(library.library_id, [])
        if book not in books_taken_from_library:
            return False
        books_taken_from_library.remove(book)
        self.books_lent[library.library_id] = books_taken_from_library
        return True

    def list_books_lent_to_reader(self, library):
        return self.books_lent.get(library.library_id, [])

    def n_books_from_library(self, library_id):
        return len(self.books_lent.get(library_id, []))

    def __hash__(self):
        return hash((self.name, self.citizen_number))

    def __eq__(self, other):
        return self.citizen_number == other.citizen_number

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Reader({self.name}, {self.citizen_number})"
