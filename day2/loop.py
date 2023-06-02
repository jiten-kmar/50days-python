user_input = "Enter the Todo: "
todos= []
i=1
while i < 3:
    todo = input(user_input)
    print(todo.capitalize())
    todos.append(todo)
    i=i+1
print("here is the final todo list:", todos)