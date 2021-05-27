# A simple python GUI example code.

import PySimpleGUI as sg
import time

# Define the window's contents
layout = [[sg.Text("Enter your weight in kg")],
          [sg.Input(key="weight")],
          [sg.Text("Enter your height in cm")],
          [sg.Input(key="height")],
          [sg.Button('Ok')],
          [sg.Text(size=(40,1),key='OUTPUT')]]

#Create the window

window = sg.Window("BMI Calculator", layout)

Event = True

while Event == True:
    #time.sleep(2)
    event, values = window.read()
    print(event)
    if event == 'Ok':
        try:
            Wt = int(values['weight'])
            Ht = int(values['height'])
            BMI = Wt/(Ht*Ht)*10000
            values["BMI"] = str(BMI)
            print(values)
            window['OUTPUT'].update("BMI is: "+values["BMI"])
        except:
            window['OUTPUT'].update("Please enter the correct values")
    else:
        print("Ohoo than podoooooo")
    if event == None:
        Event = False
        break

#window.close()


