from pydantic import BaseModel,EmailStr


class UserIn(BaseModel):
    email:EmailStr
    firstname:str
    lastname:str
    password:str

class UserOut(BaseModel):
    firstname:str
    lastname:str
    email:EmailStr
    id:int
    