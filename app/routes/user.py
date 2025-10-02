from fastapi import APIRouter, Depends, HTTPException,status
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from db_models import User
from pd_models import UserIn, UserOut, UserUpdateIn
from passlib.context import CryptContext
from uuid import UUID


user_route = APIRouter(tags=["Users Route"])


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
@user_route.get("/get_user_by_id",response_model=UserOut) # this is the endpoint
async def get_user_by_id(id: UUID, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist with the provided id"
        )    
    return user

# Creating a new item into the backend
@user_route.post("/create_user", response_model=UserOut)
async def post_user(user: UserIn, db: Session = Depends(get_db)):
    # let us hash the password first
    hashed_password = pass_context.hash(user.password)
    new_user = User(email=user.email, firstname=user.firstname, lastname=user.lastname, password=hashed_password, phonenumber=user.phonenumber)
    db.add(new_user) #telling sqlalchemy to add this to database
    db.commit() # this saves new changes in the database
    db.refresh(new_user) # this updates the user object

    return new_user

# update items in the backend
@user_route.put("/update_user", response_model=UserOut)
async def update_user(user:UserUpdateIn, db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == user.id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    db_user.phonenumber = user.phonenumber
    db.commit()
    db.refresh(db_user)
    return db_user


# delete items in the backend
@user_route.delete("/delete_user")
async def delete_user():
    return {"message": "user data deleted successfully"}