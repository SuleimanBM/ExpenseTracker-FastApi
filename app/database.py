from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# to load content of the .env file
load_dotenv()

#extract the database path
DATABASE_PATH = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_PATH)

#testing the database connection
try:
    with engine.connect() as connection:
        print("Database connection is successful")
except Exception as e:
    print("Database connection failed")
    print("Error: ", e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()