from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base
# # Set up the database engine and Base class
engine=create_engine('mysql+mysqlconnector://username:password@host/database_name')
Base=declarative_base()
# Define the User class
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String(20))
    age=Column(Integer)

# Create tables
Base.metadata.create_all(engine)
# Set up the session
Session=sessionmaker(bind=engine)
session=Session()

# Inserting data
new_user=User(name="saikrishna",age=22)
session.add(new_user)
session.commit()
# Fetching queries
users=session.query(User).all()
print(users)
