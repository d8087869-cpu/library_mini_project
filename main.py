from data.books_data import books
from library.books_functions import display_books,search_book, get_next_book_id, add_book,borrow_book, return_book, get_available_books, get_books_by_author

def display_menu():
    print("\n================================")
    print("       LIBRARY MANAGEMENT")
    print("================================")
    print("1. Display all books")
    print("2. Search book by name")
    print("3. Add new book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Display available books")
    print("7. Display books by author")
    print("8. Exit")
    print("================================")
    

def main():
    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_books(books)

        elif choice == "2":
            name = input("Enter book name: ").strip()
            if not name:
                print("Book name cannot be empty.")
                continue
            result = search_book(books, name)
            if result:
                display_books([result])
            else:
                print("Book not found.")

        elif choice == "3":
            name = input("Enter book name: ").strip()
            author = input("Enter author name: ").strip()
            year = input("Enter publication year: ").strip()
            if not name or not author:
                print("Book name and author cannot be empty.")
                continue
            
            if not year.isdigit() or int(year) <= 0:
                print("Invalid publication year.")
                continue
            
            result = add_book(books, name, author, int(year))
            if result:
                print("Book added successfully.")
            else:
                print("Book already exists.")

        elif choice == "4":
            book_id = input("Enter book ID: ").strip()

            if not book_id.isdigit() or int(book_id) <= 0:
                print("Invalid book ID.")
                continue

            result = borrow_book(books, int(book_id))
            if result:
                print("Book borrowed successfully.")
            else:
                print("Book not found or already borrowed.")


        elif choice == "5":
            book_id = input("Enter book ID: ").strip()

            if not book_id.isdigit() or int(book_id) <= 0:
                print("Invalid book ID.")
                continue

            result = return_book(books, int(book_id))

            if result:
                print("Book returned successfully.")
            else:
                print("Book not found or already available.")

        elif choice == "6":
            available_books = get_available_books(books)
            display_books(available_books)


        elif choice == "7":
            author = input("Enter author name: ").strip()

            if not author:
                print("Author name cannot be empty.")
                continue

            author_books = get_books_by_author(books, author)
            display_books(author_books)
            
            
        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 8.")


if __name__ == "__main__":
    main()
