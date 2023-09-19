import pytest
from lib.todo_list import TodoList
from lib.todo import Todo

def test_add_is_todo_instance():
    todo_list = TodoList()
    with pytest.raises(TypeError) as e:
        todo_list.add(1)
    assert str(e.value) == 'Input must be an instance of Todo'

def test_add_todo():
    todo_list = TodoList()
    todo = Todo('Buy milk')
    todo_list.add(todo)
    assert todo_list.todos == [todo]