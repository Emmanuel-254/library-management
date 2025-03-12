from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', back_populates='author')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', back_populates='category')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    author = relationship('Author', back_populates='books')
    category = relationship('Category', back_populates='books')

    @classmethod
    def create(cls, session, title, author, category):
        new_book = cls(title=title, author=author, category=category)
        session.add(new_book)
        session.commit()

    @classmethod
    def delete(cls, session, book_id):
        book = session.query(cls).get(book_id)
        if book:
            session.delete(book)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, book_id):
        return session.query(cls).get(book_id)

    @classmethod
    def find_by_attribute(cls, session, attribute, value):
        return session.query(cls).filter(getattr(cls, attribute) == value).all()