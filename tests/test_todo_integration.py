import pytest
from lib.todo import Todo
from lib.todo_list import TodoList

def test_get_incomplete_todos():
    todo_list = TodoList()
    todo1 = Todo('Buy milk')
    todo2 = Todo('Buy eggs')
    todo2.mark_complete()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1]

def test_get_complete_todos():
    todo_list = TodoList()
    todo1 = Todo('Buy milk')
    todo2 = Todo('Buy eggs')
    todo2.mark_complete()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.complete() == [todo2]

def test_give_up():
    todo_list = TodoList()
    todo1 = Todo('Buy milk')
    todo2 = Todo('Buy eggs')
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo_list.complete() == [todo1, todo2]