from models.database import engine
from models.base import Base
from models.book import Book
from models.member import Member
from models.borrowing import Borrowing

print("📌 Tables detected before creation:", 
Base.metadata.tables.keys())  # Debugging
Base.metadata.create_all(engine)  # Create tables
print("✅ Database and tables created successfully!")