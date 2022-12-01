from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .. import database,models,schemas
from ..repositories import task , user

router=APIRouter( prefix="/tasks",tags=["tasks"])

session=Session

#get all tasks
@router.get('/')
def get_all_tasks(db:session=Depends(database.get_db)):
   return task.get_all_tasks(db)
#create task
@router.post('/tasks')
def create_task(owner_id:int,request:schemas.Task,db:Session=Depends(database.get_db)):
    return task.create_task(owner_id,request,db)
#get some task
@router.get('/{id}')
def get_one_task(id:int,db:Session=Depends(database.get_db)):
   return task.get_one_task(id,db)

#update some task
@router.put('/{id}')
def update_task(id:int,request:schemas.Task,db:Session=Depends(database.get_db)):
    return task.update_task(id,request,db)

#delete some task
@router.delete('/{id}')
def delete(id:int,db:Session=Depends(database.get_db)):
    return task.delete(id,db)