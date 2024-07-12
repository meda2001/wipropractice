# library_management/book.py

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter year of publication: "))
    isbn = input("Enter book ISBN: ")
    is_available = input("Is the book available? (yes/no): ").strip().lower() == 'yes'
    book = {
        'title': title,
        'author': author,
        'year': year,
        'isbn': isbn,
        'is_available': is_available
    }
    books.append(book)
    print(f"Book '{title}' added successfully.")

def update_book(books):
    title = input("Enter the title of the book to update: ")
    for book in books:
        if book['title'] == title:
            book['author'] = input("Enter new author: ")
            book['year'] = int(input("Enter new year of publication: "))
            book['isbn'] = input("Enter new ISBN: ")
            book['is_available'] = input("Is the book available? (yes/no): ").strip().lower() == 'yes'
            print(f"Book '{title}' updated successfully.")
            return
    print(f"Book '{title}' not found.")

def delete_book(books):
    title = input("Enter the title of the book to delete: ")
    for i, book in enumerate(books):
        if book['title'] == title:
            del books[i]
            print(f"Book '{title}' deleted successfully.")
            return
    print(f"Book '{title}' not found.")

def view_books(books):
    if not books:
        print("No books to display.")
        return
    for book in books:
        print(book)

def search_book(books):
    search_by = input("Search by title or author? (title/author): ").strip().lower()
    if search_by not in ['title', 'author']:
        print("Invalid search option.")
        return

    search_term = input(f"Enter the {search_by}: ").strip()
    for book in books:
        if book[search_by] == search_term:
            print(book)
            return
    print(f"No book found with {search_by} '{search_term}'.")

def generate_report(books):
    if not books:
        print("No books to generate report.")
        return
    print(f"Total number of books: {len(books)}")
    
    year = int(input("Enter year to list books published after: "))
    print(f"Books published after {year}:")
    for book in books:
        if book['year'] > year:
            print(book)
