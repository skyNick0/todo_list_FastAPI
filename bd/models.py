from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from todo_database import Base


class TodoList(Base):
    __tablename__ = "todo_lists"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    tasks = relationship("Task", back_populates="todo_list")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    todo_list_id = Column(Integer, ForeignKey("todo_lists.id"))

    todo_list = relationship("TodoList", back_populates="tasks")

class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    todo_list_id = Column(Integer, ForeignKey("todo_lists.id"))
    todo_list = relationship("TodoList", back_populates="users")

