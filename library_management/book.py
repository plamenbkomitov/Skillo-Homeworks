class Book:
    def __init__(self, title, author, genre, isbn):
        self.isbn = isbn
        self.genre = genre
        self.author = author
        self.title = title

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title
