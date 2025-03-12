from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base 

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
