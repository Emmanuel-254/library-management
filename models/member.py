from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base  #Import Base

class Member(Base):  #Inherit from Base
    __tablename__ = 'members'  #Ensure _tablename_ is defined

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    books = relationship("Book", back_populates="member")
    borrowings = relationship("Borrowing", back_populates="member", cascade="all, delete-orphan")

    def _repr_(self):
        return f"<Member(id={self.id}, name='{self.name}', email='{self.email}')>"