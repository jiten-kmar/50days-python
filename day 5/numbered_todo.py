todos = []

while True:
    user_action = input("Type add or show or edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("No of todos to edit"))
            number = number -1
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of todo to complete"))
            todo.pop(number-1)
        case 'exit':
            break


