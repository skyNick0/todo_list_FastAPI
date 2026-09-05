from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from bd.models import Task as TaskModel
from bd.models import TodoList as TodoListModel
from bd.schema import TaskCreate, TaskResponse
from bd.todo_database import get_db


router = APIRouter()


@router.post(
    "/tasks/add",
    tags=["tasks"],
    response_model=TaskResponse
)
def add_task(
    new_task: TaskCreate,
    db: Session = Depends(get_db)
):
    todo = db.query(TodoListModel).filter(
        TodoListModel.id == new_task.todo_list_id
    ).first()

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo list not found"
        )

    task = TaskModel(
        title=new_task.title,
        todo_list_id=new_task.todo_list_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task