FILEPATH = "TODOS.txt"

def write_todo(todo_list):
    with open(FILEPATH, 'w') as file:
        file.writelines(todo_list)

def read_todo():
    with open(FILEPATH) as file:
        data = file.readlines()
    return data