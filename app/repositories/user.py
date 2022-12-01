from sqlalchemy.orm import session
from .. import schemas,models

def create_user(request:schemas.User,db:session):
    new_user=models.User(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:session):
    users=db.query(models.User).all()
    return users

def get_one_user(id:int,db:session):
    user=db.query(models.User).filter(models.User.id==id).first()
    return user