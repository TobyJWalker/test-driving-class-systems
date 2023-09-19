from lib.todo import Todo

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        if type(todo) != Todo:
            raise TypeError('Input must be an instance of Todo')
        self.todos.append(todo)

    def incomplete(self):
        return [todo for todo in self.todos if not todo.complete]

    def complete(self):
        return [todo for todo in self.todos if todo.complete]

    def give_up(self):
        for todo in self.todos:
            todo.mark_complete()