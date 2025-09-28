from fastapi import FastAPI, Depends
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from db_models import User
from pd_models import UserIn, UserOut
from passlib.context import CryptContext

Base.metadata.create_all(bind=engine)

myapp = FastAPI()


# function to retrieve database session:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# creating a password context variable
pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Get something from backend
@myapp.get("/get_user") # this is the endpoint
async def get_user():
    return {"message": "user data accessed successfully."}

# Creating a new item into the backend
@myapp.post("/create_user", response_model=UserOut)
async def post_user(user: UserIn, db: Session = Depends(get_db)):
    # let us hash the password first
    hashed_password = pass_context.hash(user.password)
    new_user = User(email=user.email, firstname=user.firstname, lastname=user.lastname, password=hashed_password)
    db.add(new_user) #telling sqlalchemy to add this to database
    db.commit() # this saves new changes in the database
    db.refresh(new_user) # this updates the user object

    return new_user

# update items in the backend
@myapp.put("/update_user")
async def update_user():
    return {"message": "user data updated successfully"}

# delete items in the backend
@myapp.delete("/delete_user")
async def delete_user():
    return {"message": "user data deleted successfully"}