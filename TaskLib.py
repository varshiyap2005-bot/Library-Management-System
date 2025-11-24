class Library:
    def __init__(self):
        self.books = {}
        self.issued_books = set()

    def add_book(self):
        try:
            book = input("Enter book name to add: ")
            if book in self.books:
                print("Book already exists.")
            else:
                self.books[book] = "Available"
                print("Book added.\n")
        except Exception as e:
            print("Error:", e)

    def display_books(self):
        if not self.books:
            print("No books available.\n")
        else:
            print("Books in Library:")
            for book, status in self.books.items():
                print(f"{book} - {status}")
            print()

    def issue_book(self):
        book = input("Enter book name to issue: ")
        if book in self.books and self.books[book] == "Available":
            self.books[book] = "Issued"
            self.issued_books.add(book)
            print("Book issued.\n")
        else:
            print("Book not available.\n")
    
    def return_book(self):
        book = input("Enter book name to return: ")
        if book in self.issued_books:
            self.books[book] = "Available"
            self.issued_books.remove(book)
            print("Book returned.\n")
        else:
            print("Book was not issued.\n")


    def search_book(self):
        book = input("Enter book name to search: ")
        if book in self.books:
            print(f"Book '{book}' is available.\n")
        else:
            print(f"Book '{book}' not found.\n")

    def delete_book(self):
        book = input("Enter book name to delete: ")
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' deleted.\n")
        else:
            print(f"Book '{book}' not found.\n")
 

lib = Library()

while True:
    print("1. Add Book\n2. Display Books\n3. Issue Book\n4. Return Book\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        lib.add_book()
    elif choice == '2':
        lib.display_books()
    elif choice == '3':
        lib.issue_book()
    elif choice == '4':
        lib.return_book()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice.\n")
