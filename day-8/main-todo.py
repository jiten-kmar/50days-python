while True:
    user_action = input("Type add, show, edit, complete or exit:  ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter the todo: ") + "\n"
            with open('todos.txt','r') as file: # this makes sure it closes the file automatically
                todos = file.readlines() 
            
            todos.append(todo)
            
            with open('todos.txt','w') as file:
                file.writelines(todos) 

        case 'show':
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number which needs to be edited:  "))
            number = number - 1

            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"
            
            with open('todos.txt','w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of  todos to complete: "))
            
            with open('todos.txt','r') as file:
                todos = file.readlines()
            index= number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            with open('todos.txt','w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
                
        case 'exit':
            exit()