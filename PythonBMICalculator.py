# A simple python GUI example code.

import PySimpleGUI as sg
import time

# Define the window's contents
layout = [[sg.Text("Enter your weight in kg")],
          [sg.Input(key="weight")],
          [sg.Text("Enter your height in cm")],
          [sg.Input(key="height")],
          [sg.Text("Enter your required BMI")],
          [sg.Input(key="ReqBMI")],
          [sg.Button('Ok')],
          [sg.Button('Ideal weight')],
          [sg.Text(size=(60,1),key='Weight')],
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
            Wt = float(values['weight'])
            Ht = float(values['height'])
            BMI = Wt/(Ht*Ht)*10000
            values["BMI"] = str(BMI)
            print(values)
            window['OUTPUT'].update("BMI is: "+values["BMI"])
        except:
            window['OUTPUT'].update("Please enter the correct values")
    elif event == "Ideal weight":
        try:
            Ht = float(values['height'])
            Wt = float(values['weight'])
            ReqBMI = float(values['ReqBMI'])
            ReqWt = ReqBMI * Ht*Ht/10000
            Wtloss = Wt - ReqWt
            values["ReqWt"] = str(ReqWt)
            values["Wtloss"] = str(Wtloss)
            window['Weight'].update("Req Wt is :"+ values["ReqWt"]+" You have to loose : " + values["Wtloss"])
        except:
            window['Weight'].update("Please enter the correct values")



    if event == None:
        Event = False
        break

#test

#window.close()
