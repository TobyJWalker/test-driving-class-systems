class Todo:
    def __init__(self, task):
        if type(task) != str:
            raise TypeError('Task must be a string')
        elif task == "" or task.isspace():
            raise ValueError('Task cannot be empty')
        else:
            self.task = task
            self.complete = False

    def mark_complete(self):
        self.complete = True