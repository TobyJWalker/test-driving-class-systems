

>> TESTS

>> When creating a Todo, the task should be a string
todo = Todo(1) raises TypeError

>> When creating a todo, the task should not be empty
todo = Todo('') raises ValueError
todo = Todo('   ') raises ValueError

>> When creating a Todo, the task should be assigned
todo = Todo('task')
todo.task => 'task'

>> When creating a todo, the task should be uncompleted by default
todo = Todo('task')
todo.completed => False

>> When marking a todo as completed, the todo should be marked as completed
todo = Todo('task')
todo.mark_completed()
todo.completed => True

>> When adding a todo to the todolist, the todo should be of type Todo
todolist = TodoList()
todolist.add(1) raises TypeError

>> When adding a todo, it should be added to the list
todolist = TodoList()
todo = Todo('task')
todolist.add(todo)
todolist.todos => [todo]

>> When viewing a list of incomplete todos, only incomplete todos should be shown (Integration)
todolist = TodoList()
todo1 = Todo('task1')
todo2 = Todo('task2')
todo2.mark_completed()
todolist.incomplete() => [todo1]

>> When viewing a list of complete todos, only complete todos should be shown (Integration)
todolist = TodoList()
todo1 = Todo('task1')
todo2 = Todo('task2')
todo2.mark_completed()
todolist.complete() => [todo2]

>> When giving up, all todos should be marked as complete (Integration)
todolist = TodoList()
todo1 = Todo('task1')
todo2 = Todo('task2')
todolist.give_up()
todo1.completed => True
todo2.completed => True