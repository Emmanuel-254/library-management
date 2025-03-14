from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    _tablename_ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    transactions = relationship('Transaction', back_populates='user', cascade='all, delete-orphan')

    def _repr_(self):
        return f"<User(id={self.id}, name='{self.name}')>"