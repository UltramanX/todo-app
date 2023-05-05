import functions
import PySimpleGUI as sg
import time

# change theme
sg.theme(
    'DarkAmber'
)
# elements
label_clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
# list_box = sg.Listbox(values=functions.get_todos(), key='todos',
#                       enable_events=True, size=[45, 10])
list_box = sg.Listbox(values=[todo.rstrip() for todo in functions.get_todos()], key='todos',
                      enable_events=True, size=[45, 10])


edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# create instance of a window type
window = sg.Window('My To-Do App',
                   layout=[[label_clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=20)
    window["clock"].update(value=time.strftime("%b %d,  %Y %H:%M:%S"))
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case "Edit":
            try:
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
            except IndexError:
                sg.popup("Please select and item first.", font=("Helvetica", 15))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select and item first.", font=("Helvetica", 15))

        case sg.WIN_CLOSED:
            break


window.close()
