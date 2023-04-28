import functions
import PySimpleGUI as sg

# elements
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# create instance of a window type
window = sg.Window('My To-Do App', layout=[[[label], [input_box, add_button]]])
window.read()
window.close()
