from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str


class TodoList(BaseModel):
    todo_id: int
    todo_name: str


class Task(BaseModel):
    task_id: int
    task_name: str