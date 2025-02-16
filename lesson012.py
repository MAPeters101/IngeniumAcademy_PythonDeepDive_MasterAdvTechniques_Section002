"""
Object Length: len

Enable the built-in len() function for custom objects.
"""

class Library:
    def __init__(self, books, librarians):
        self.books = books
        self.librarians = librarians

    def __len__(self):
        return len(self.librarians) + len(self.books)


if __name__ == '__main__':
    lib = Library(books=["book1", "book2"],
                  librarians=['librarian1', 'librarian2'])
    print(len(lib))


