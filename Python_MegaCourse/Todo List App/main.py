todos = []

while True:
    user_action = input("Enter 'add', 'show' or 'exit': ").lower()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            if not todos:
                print("There is nothing in the list.")
            else:
                for index, todo in enumerate(todos, start=1):
                    print(f"{index}. {todo}")
        case 'exit':
            print('Exiting...')
            break
        case _:
            print("Please enter a valid option.")