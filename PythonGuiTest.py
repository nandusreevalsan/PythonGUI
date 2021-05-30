# A simple python GUI example code.
# A Nandu Sreevalsan production
import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What about your name?")],
          [sg.Input()],
          [sg.Button('Ok')],
          [sg.Button('Podooo')]]

#Create the window

window = sg.Window("Chumma Test", layout)

event, values = window.read()

if event == 'Ok':
    print('Hello', values[0], "Thanks for trying my code")
else:
    print("Ohoo than podoooooo")


window.close()
