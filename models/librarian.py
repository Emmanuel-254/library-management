from sqlalchemy import Column, Integer, String
from models.base import Base

class Librarian(Base):
    __tablename__ = 'librarians'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def _repr_(self):
        return f"<Librarian(id={self.id}, name='{self.name}', email='{self.email}')>"