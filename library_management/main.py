from book import Book
from library import Library
from reader import Reader

b1 = Book(
    title="East of Eden",
    author="John Steinbeck",
    genre="Historical fiction",
    isbn="9823473BJDJFG87",
)

b2 = Book(
    title="Dune",
    author="Franck Herbert",
    genre="Science fiction",
    isbn="45623473BJDJFG87",
)

b3 = Book(
    title="Dune",
    author="Franck Herbert",
    genre="Science fiction",
    isbn="45623473BJDJFG87",
)

library = Library("Test library", "L1")
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

pesho = Reader("Peter", "094959865")
gosho = Reader("George", "04669865")

library.subscribe_reader(pesho)
library.subscribe_reader(gosho)
for r in library.readers:
    print(r)
print(library.readers)
print()
print(f"Books from library before lending:")
for book in library.books:
    print(book)
print()

library.lend_book(b2, pesho)
print(f"Books from library after lending:")
for book in library.books:
    print(book)
print()

print(f"Lent Books to {pesho}:")
for book in library.list_books_lent_to_reader(pesho):
    print(book)
print()

for r in library.readers:
    print(r)
print(library.readers)
print()
print(f"Books from library before returning:")
for book in library.books:
    print(book)
print()

library.return_book(b2, pesho)
print(f"Books from library after returning:")
for book in library.books:
    print(book)
print()

print(f"Lent Books to {pesho}:")
for book in library.list_books_lent_to_reader(pesho):
    print(book)
print()

library.unsubscribe_reader(gosho)
print(library.readers)
