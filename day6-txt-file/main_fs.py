while True:
    user_action = input("Type add, show, edit complete or exit:  ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter the todo: ") + "\n"
            file = open('todos.txt','r')    
            todos = file.readlines() 
            todos.append(todo)
            file.close()    
            
            file = open('todos.txt','w')    
            file.writelines(todos) 
            file.close()    
        case 'show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()    
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