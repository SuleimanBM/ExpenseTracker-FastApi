from sqlalchemy import Column,String,Integer,Float
from app.database import Base
import uuid #it is the python uuid
from sqlalchemy.dialects.postgresql import UUID
#The user class
class User(Base):
    #giving the table a name
    __tablename__ = "users"
    #defining relevant columns in the table
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True,)
    firstname = Column(String(20))
    lastname = Column(String(20))
    password = Column(String)
    phonenumber = Column(String())


