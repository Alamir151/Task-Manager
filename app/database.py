from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os 
from sqlalchemy.orm import sessionmaker
from dotenv import load
load('.env')



SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
#
engine = create_engine(
    f"{SQLALCHEMY_DATABASE_URL}",  echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
        
