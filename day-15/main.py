from functions import get_todos,write_todos
# import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("it is :", now)
while True:
    user_action = input("Type add, show, edit, complete or exit:  ")
    user_action = user_action.strip()

    if  user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        
        todos = get_todos()
        
        todos.append(todo)

        write_todos(todos )

    elif user_action.startswith('show'):
    
        todos = get_todos()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index +1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            
            number = int(user_action[5:])
            number = number - 1
            
            todos = get_todos()
            
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"
            
            write_todos(todos)

        except ValueError:
            print("command entered is not valid.")
            # user_action = input("Type add, show, edit, complete or exit:  ")
            # user_action = user_action.strip()
            continue
            
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos = get_todos()
            
            index= number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number and seems out of range.")
            continue
                 
    elif 'exit' in user_action:
        exit()
    else:
        print("command is not valid")
        
print("Bye")