todos = []
while True:
    user_action = input("Type add, show, edit complete or exit:  ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter the todo: ")
            todos.append(todo)      
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index +1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number which needs to be edited:  "))
            number = number - 1
            new_item = input("Enter the item: ")
            todos[number] = new_item
        case 'complete':
            number = int(input("Number of  todos to complete: "))
            todos.pop(number-1)
        case 'exit':
            exit()