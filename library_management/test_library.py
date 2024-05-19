from book import Book
from library import Library


def make_a_book():
    return Book(
        title="East of Eden",
        author="John Steinbeck",
        genre="Historical fiction",
        isbn="9823473BJDJFG87",
    )


def test_create_empty_library():
    library = Library("Test library")
    assert len(library.books) == 0


def test_add_book_to_library():
    book = make_a_book()
    library = Library("Test library")
    library.add_book(book)
    assert len(library.books) == 1


def test_delete_book_from_library():
    book1 = make_a_book()
    book2 = make_a_book()

    library = Library("Test library")
    library.add_book(book1)
    library.add_book(book2)

    library.delete_all_copies_of_book(book1)

    assert len(library.books) == 0


