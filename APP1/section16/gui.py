import functions
import PySimpleGUI as sg

# elements
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
# list_box = sg.Listbox(values=functions.get_todos(), key='todos',
#                       enable_events=True, size=[45, 10])
list_box = sg.Listbox(values=[todo.rstrip() for todo in functions.get_todos()], key='todos',
                      enable_events=True, size=[45, 10])


edit_button = sg.Button("Edit")

# create instance of a window type
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],[list_box, edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0].rstrip()
            new_todo = values['todo']

            # get current todos from functions
            #todos = functions.get_todos()
            todos = [todo.rstrip() for todo in functions.get_todos()]

            # replace existing with new Todos
            index = todos.index(todo_to_edit)

            # update todos list
            todos[index] = new_todo

            # write it down
            functions.write_todos(todos)

            # update and display it on win
            window['todos'].update(values=todos)

        # case "todos":
        #     window['todo'].update(values=values['todos'][0])



        case sg.WIN_CLOSED:
            break


window.close()
