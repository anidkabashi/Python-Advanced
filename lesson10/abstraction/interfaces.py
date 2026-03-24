from abc import ABC, abstracmethod

class Printable(ABC):

    @abstractmethode
    def print_info(self):
        pass

class Book(Printable):
    def __init(self, title, author):
        self.title=title
        self.author=author

    def print_info(self):
        print(f"Book: {self.title} by {self.author}")

book = Book("The great Gatsby", "f. Scoot Fitzgerald")
book.print_info()