def get_todos(filepath="todos.txt"):
    """
    read the lines
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_args,filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_args)


print(help(get_todos()))

print(__name__) #
## below lines will not execute from main.py if provided this way

if (__name__) == "__main__":
    print("hello")
    print(get_todos())