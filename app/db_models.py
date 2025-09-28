from sqlalchemy import Column,String,Integer,Float
from database import Base,engine


#The user class
class User(Base):
    #giving the table a name
    __tablename__ = "users"
    #defining relevant columns in the table
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True,)
    firstname = Column(String(20))
    lastname = Column(String(20))
    password = Column(String)


