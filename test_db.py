from sqlalchemy.orm import sessionmaker
from models.database import session, engine
from models.member import Member

Session = sessionmaker(bind=engine)
session = Session()

# Check if a member with the email already exists
existing_member = session.query(Member).filter_by(email="johndoe@gmail.com").first()

if not existing_member:
    new_member = Member(name="John Doe", email="johndoe@gmail.com")
    session.add(new_member)
    session.commit()
    print("Member added successfully!")
else:
    print("Member already exists!")

# Fetch all members to verify
members = session.query(Member).all()
print(f"Members in database: {[member.name for member in members]}")