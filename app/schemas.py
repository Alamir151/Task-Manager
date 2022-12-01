from pydantic import EmailStr
from pydantic import BaseModel,Field
from typing import Union
from typing import List,Union
class Task(BaseModel):
    
    
    title:str
    body:str
    completed:bool
    class Config:
        orm_mode=True
    
    
class User(BaseModel):
   
    name:str
    email:EmailStr
    password:str
    
    class Config:
        orm_mode=True
    

class ShowUser(BaseModel):
    name: Union[str,None]=Field(
        default=None, title="The description of the item", max_length=300
    )
   
    email:Union[str,None]=Field(
        default=None, title="The description of the item", 
    )
    tasks:List[Task]=[]
    class Config:
        orm_mode=True