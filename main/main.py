from fastapi import FastAPI

from bd.todo_database import Base, engine
from bd import models

from routes.users import router as users_router
from routes.todos import router as todos_router
from routes.task import router as tasks_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)
app.include_router(todos_router)
app.include_router(tasks_router)