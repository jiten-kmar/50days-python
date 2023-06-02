# todos = []

# while True:
#     user_action = input("Type add or show or edit or exit: ")
#     user_action = user_action.strip()
#     if user_action == 'add':
#         todo=input("Enter todo: ")
#         todos.append(todo)
#     elif user_action == 'show':
#         print(todos)
#     elif user_action == 'edit':
#         number = int(input("Please enter the number of todo list to edit: "))
#         number = number - 1
#         existing_todo = todos[number]
#         todos[number] = input("Please enter the a new todo")
#         print(existing_todo)
#     else:
#         print("Bye")
#         print("final todo list is:", todos)
#         break
todos = []

while True:
    user_action = input("Type add or show or edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo=input("Enter todo: ")
            todos.append(todo)
        case 'show':
            for items in todos:
                print(items)
        case 'exit':
            break
print("Good bye")