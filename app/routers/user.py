from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from .. import database,models,schemas
from ..repositories import user
router=APIRouter( prefix="/users",tags=["users"])






@router.get('/{id}',response_model=schemas.ShowUser)
def get_one_user(id:int,db:Session=Depends(database.get_db)):
   return user.get_one_user(id,db)


#create user
@router.post('/')
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
    return user.create_user(request,db)
