# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor that initializes book details"""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book created: {self.title} by {self.author}, {self.year}")

    def __str__(self):
        """User-friendly string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official developer representation"""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor message when object is deleted"""
        print(f"Deleting {self.title}")
