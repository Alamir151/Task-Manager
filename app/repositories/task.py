from sqlalchemy.orm import session
from .. import models,schemas
from fastapi import HTTPException

def get_all_tasks(db:session):
    tasks=db.query(models.Task).all()
    return tasks

def create_task(owner_id:int,request:schemas.Task,db:session):
    new_task=models.Task(title=request.title,body=request.body,completed=request.completed,owner_id=owner_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_one_task(id:int,db:session):
    task=db.query(models.Task).filter(models.Task.id==id)
    if not task.first():
        raise HTTPException(status_code=404, detail="not found task")
    return task.first()

def update_task(id:int,request:schemas.Task,db:session):
    task=db.query(models.Task).filter(models.Task.id==id)
    if not task.first():
        raise HTTPException(status_code=404, detail="not found Task")
    task.update({'title':request.title,'body':request.body,'completed':request.completed})
    db.commit()
    return f'update task with id {id}'

def delete(id:int,db:session):
    db.query(models.Task).filter(models.Task.id==id).delete(synchronize_session=False)
    return 'deleted task with id {id}'