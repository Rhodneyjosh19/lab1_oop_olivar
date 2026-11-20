class Book:
    total_books = 0

    def __init__(self, title, author, isbn, is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        Book.total_books += 1

    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title}' is unavailable. It is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'.")

    def return_book(self):
        self.is_borrowed = False
        print(f"'{self.title}' has been returned.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    def __repr__(self):
        return f"Book(title='{self.title}', isbn='{self.isbn}')"


if __name__ == "__main__":
    books = [
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353427"),
        Book("The Hobbit", "J.R.R. Tolkien", "9780547928227"),
        Book("The Hunger Games", "Suzanne Collins", "9780439023528"),
        Book("The Alchemist", "Paulo Coelho", "9780062315007"),
    ]

    books[0].borrow()
    books[0].borrow()
    books[2].borrow()
    books[0].return_book()

    print("\nAll books:")
    for book in books:
        print(book)

    print("\nRepr of first book:", repr(books[0]))
    print("Total books:", Book.total_books)