from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base  #Import Base

class Borrowing(Base):  #Inherit from Base
    __tablename__ = 'borrowings'  #Ensure _tablename_ is defined

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    member_id = Column(Integer, ForeignKey('members.id'))

    book = relationship("Book", back_populates="borrowings")
    member = relationship("Member", back_populates="borrowings")

    def _repr_(self):
        return f"<Borrowing(id={self.id}, book_id={self.book_id}, member_id={self.member_id})>"