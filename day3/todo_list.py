todos = []

while True:
    user_action = input("Type add or show or exit: ")
    if user_action == 'add':
        todo=input("Enter todo: ")
        todos.append(todo)
    elif user_action == 'show':
        print(todos)
    else:
        print("Bye")
        print("final todo list is:", todos)
        break