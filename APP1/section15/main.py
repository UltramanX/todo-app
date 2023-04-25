from functions import get_todos, write_todos
import time

text = """
Principles of Productivity:
This is a multiline string
This is a second multiline string
"""

text = "\
Principles of Productivity: \
This is a single line string \
This is a second single line string \
"

now = time.strftime("%b %d, - %Y %H:%M:%S")
print("It's", now)

while True:
    user_action = input("Type add, show, edit, remove or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for i, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{i + 1}.-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[6:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Entered Item doesn't exits, try again!")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!")

print("Bye!")
