"""
Object Length: len

Enable the built-in len() function for custom objects.
"""

class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)




