def display_books(books):
    if not books:
        print("NO BOOKS FOUND")
        return
    for book in books:
        print("==============================")
        print(f"ID: {book['id']}")
        print(f"Name: {book['name']}")
        print(f"Auther: {book['author']}")
        print(f"Year: {book['year']}")
        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Borrowed")
        print("==============================")


def search_book(books, name):
    for book in books:
        if name.lower() in book["name"].lower():
            return book 
    return None


def get_next_book_id(books):
    pass
    if not books:
        return 1
    max_id = books[0]["id"]
    for book in books:
        if book["id"] > max_id:
            max_id = book["id"]
    return max_id +1



def add_book(books, name, author, year):
    if not name.strip() or not author.strip():
        return False
    if year <= 0:
        return False
    for book in books:
        if book["name"].lower() == name.strip().lower() and book["author"].lower() == author.strip().lower():
            return False
        
    new_book = {
        "id": get_next_book_id(books),
        "name": name.strip(),
        "author": author.strip(),
        "year": year,
        "available": True}
    books.append(new_book)
    return True



def borrow_book(books, book_id):
    for book in books:
        if book["id"] == book_id:

            if not book["available"]:
                return False

            book["available"] = False
            return True

    return False



def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:

            if book["available"]:
                return False

            book["available"] = True
            return True

    return False



def get_available_books(books):
    available_books = []

    for book in books:
        if book["available"]:
            available_books.append(book)

    return available_books



def get_books_by_author(books, author):
    author_books = []

    for book in books:
        if author.lower() in book["author"].lower():
            author_books.append(book)

    return author_books
