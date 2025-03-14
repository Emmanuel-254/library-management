from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.base import Base

# Database URL
DATABASE_URL = "sqlite:///library.db"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session factory
Session = sessionmaker(bind=engine)

# Initialize database
def init_db():
    Base.metadata.create_all(engine)