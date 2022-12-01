from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    tasks=relationship("Task",back_populates="created_by")
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    completed=Column(Boolean,default=False)
    owner_id= Column(Integer, ForeignKey("users.id"))

    created_by = relationship("User",back_populates="tasks") 
    
    
    
