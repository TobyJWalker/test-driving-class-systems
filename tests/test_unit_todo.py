import pytest
from lib.todo import Todo

def test_task_not_string():
    with pytest.raises(TypeError) as e:
        Todo(1)
    assert str(e.value) == 'Task must be a string'

def test_task_is_empty():
    with pytest.raises(ValueError) as e:
        Todo('')
    assert str(e.value) == 'Task cannot be empty'

def test_task_is_space():
    with pytest.raises(ValueError) as e:
        Todo(' ')
    assert str(e.value) == 'Task cannot be empty'

def test_task_assigned():
    todo = Todo('Buy milk')
    assert todo.task == 'Buy milk'

def test_marked_incomplete():
    todo = Todo('Buy milk')
    assert todo.complete == False

def test_marked_complete():
    todo = Todo('Buy milk')
    todo.mark_complete()
    assert todo.complete == True