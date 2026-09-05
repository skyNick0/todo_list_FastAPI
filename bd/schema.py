from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)


class TodoListCreate(BaseModel):
    title: str




class TaskCreate(BaseModel):
    title: str
    todo_list_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    todo_list_id: int

    model_config = ConfigDict(from_attributes=True)

class TodoListResponse(BaseModel):
    id: int
    title: str
    tasks: list[TaskResponse] = []

    model_config = ConfigDict(from_attributes=True)
