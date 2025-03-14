from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base  

class Book(Base):  
    __tablename__ = 'books'  

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=True)

    member = relationship("Member", back_populates="books")
    borrowings = relationship("Borrowing", back_populates="book", cascade="all, delete-orphan")

    def _repr_(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"
    
    from models.borrowing import Borrowing