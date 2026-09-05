from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from bd.models import TodoList as TodoListModel
from bd.schema import TodoListCreate, TodoListResponse
from bd.todo_database import get_db


router = APIRouter()


@router.post(
    "/todos/create",
    tags=["todos"],
    response_model=TodoListResponse
)
def todo_create(
    new_todo: TodoListCreate,
    db: Session = Depends(get_db)
):
    todo = TodoListModel(
        title=new_todo.title
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


@router.get(
    "/todos",
    tags=["todos"],
    response_model=list[TodoListResponse]
)
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoListModel).all()

    return todos

@router.get(
    "/todos/{title}",
    tags=["todos"],
    response_model=TodoListResponse
)
def get_todo_by_title(
    title: str,
    db: Session = Depends(get_db)
):
    todo = db.query(TodoListModel).filter(
        TodoListModel.title == title
    ).first()

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo list not found"
        )

    return todo
