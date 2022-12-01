from fastapi import FastAPI


from . import database,models,schemas
from .database import engine
app=FastAPI()
models.Base.metadata.create_all(engine)
from .routers import task,user


app.include_router(task.router)
app.include_router(user.router)


