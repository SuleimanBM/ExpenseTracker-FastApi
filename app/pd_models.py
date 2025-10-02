from pydantic import BaseModel,EmailStr
from uuid import UUID


class UserIn(BaseModel):
    email:EmailStr
    firstname:str
    lastname:str
    password:str
    phonenumber:str

class UserOut(BaseModel):
    firstname:str
    lastname:str
    email:EmailStr
    id:UUID
    phonenumber:str

# model for updates coming
class UserUpdateIn(BaseModel):
    id:UUID
    phonenumber:str