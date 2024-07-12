# library_main.py

from library_management.book import (
    add_book, update_book, delete_book,
    view_books, search_book, generate_report
)

def main():
    books = []
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View All Books")
        print("5. Search for a Book")
        print("6. Generate Report")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            update_book(books)
        elif choice == '3':
            delete_book(books)
        elif choice == '4':
            view_books(books)
        elif choice == '5':
            search_book(books)
        elif choice == '6':
            generate_report(books)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
