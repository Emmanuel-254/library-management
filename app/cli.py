import sys
from app.db import Session 
from app.models import Author, Book, Category 

def show_menu():
    print("\nLibrary Management CLI")
    print("1. Create Book")
    print("2. Delete Book")
    print("3. View All Books")
    print("4. View Book by ID")
    print("5. Exit")

def main():
    session = Session()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':  # Create Book
            title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            category_name = input("Enter book category: ")

            # Find or create author
            author = session.query(Author).filter(Author.name == author_name).first()
            if not author:
                author = Author(name=author_name)
                session.add(author)
                session.commit()

            # Find or create category
            category = session.query(Category).filter(Category.name == category_name).first()
            if not category:
                category = Category(name=category_name)
                session.add(category)
                session.commit()

            # Create the book
            Book.create(session, title, author, category)

        elif choice == '2':  # Delete Book
            book_id = int(input("Enter book ID to delete: "))
            Book.delete(session, book_id)

        elif choice == '3':  # View All Books
            books = Book.get_all(session)
            for book in books:
                print(f"{book.id}: {book.title}, Author: {book.author.name}, Category: {book.category.name}")

        elif choice == '4':  # View Book by ID
            book_id = int(input("Enter book ID: "))
            book = Book.find_by_id(session, book_id)
            if book:
                print(f"Book ID: {book.id}\nTitle: {book.title}\nAuthor: {book.author.name}\nCategory: {book.category.name}")
            else:
                print("Book not found!")

        elif choice == '5':  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
