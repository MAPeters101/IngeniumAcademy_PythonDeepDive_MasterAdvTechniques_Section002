"""
Basic Representation: __repr__ and __str__

These methods determine the human-readable and unambiguous string
representation of an object
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self): # for developers
        return f"Book('{self.title}',  '{self.author}')"

    # def __str__(self): # for end user
    #     return f"'{self.title}' by {self.author}"


if __name__ == '__main__':
    book = Book("1984", "George Orwell")
    print(repr(book))

    #print(eval(repr(book)).title)

    print(str(book))

