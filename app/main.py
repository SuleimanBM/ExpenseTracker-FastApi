from fastapi import FastAPI
from database import engine
from db_models import  Base
from routes import user, transactions

Base.metadata.create_all(bind=engine)

myapp = FastAPI()

# including routes here
myapp.include_router(user.user_route)
myapp.include_router(transactions.transaction_route)