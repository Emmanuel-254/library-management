from models.book import Book
from models.member import Member
from models.librarian import Librarian
from models.borrowing import Borrowing
from models.database import session
from datetime import datetime

def create_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    
    new_book = Book(title=title, author=author)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' added successfully!")

def create_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    
    new_member = Member(name=name, email=email)
    session.add(new_member)
    session.commit()
    print(f"Member '{name}' added successfully!")

def create_librarian():
    name = input("Enter librarian name: ")
    email = input("Enter librarian email: ")
    
    new_librarian = Librarian(name=name, email=email)
    session.add(new_librarian)
    session.commit()
    print(f"Librarian '{name}' added successfully!")

def borrow_book():
    member_id = int(input("Enter Member ID: "))
    book_id = int(input("Enter Book ID: "))

    book = session.query(Book).filter_by(id=book_id).first()
    if book and not book.member_id:
        borrowing = Borrowing(member_id=member_id, book_id=book_id)
        book.member_id = member_id
        session.add(borrowing)
        session.commit()
        print(f"Book borrowed successfully!")
    else:
        print("Book is already borrowed or does not exist.")

def return_book():
    borrowing_id = int(input("Enter Borrowing ID: "))
    borrowing = session.query(Borrowing).filter_by(id=borrowing_id).first()
    
    if borrowing and not borrowing.returned_at:
        borrowing.returned_at = datetime.utcnow()
        session.commit()
        print("Book returned successfully!")
    else:
        print("Invalid borrowing record.")

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Add Librarian")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            create_book()
        elif choice == "2":
            create_member()
        elif choice == "3":
            create_librarian()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            break