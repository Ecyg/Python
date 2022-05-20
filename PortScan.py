import PySimpleGUI as sg
import socket
import subprocess
import sys
from datetime import datetime

#Define the layout
layout = [
    [sg.Text("Enter the Server IP Address       "), sg.Input(key="-IP_Address-")],
    [sg.Text("Enter the number of ports,\nstarting from 0, you wish to scan"), sg.Input(key="-Port_Number-")],
    [sg.Button("Scan", key="-Enter-"), sg.Button("Exit", key="-Exit-")],
    [sg.Output(size=(110,30))]
]

#Open the window
window = sg.Window("Simple Port Scanner", layout, return_keyboard_events=True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def port_scan(host,port):
    try:
        con = s.connect((host,port)) # This tuple needs the IP and port fed into the text boxes
        return True
    except:
        return False



# The program never finishes, so fix this. Python just times out. 
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == "-Exit-":
        break
    if event == "-Enter-":
        #sg.popup(value["-IP_Address-"], value["-Port_Number-"])
        for x in range(int(value["-Port_Number-"])):
            if port_scan(value["-IP_Address-"], x):
                print('Port', x, 'is open')
window.close()