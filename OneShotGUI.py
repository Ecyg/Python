import PySimpleGUI as sg
import base64
import codecs

# STEP 1 - create the window, read the window, close the window.
event, values = sg.Window('My single-line GUI!',
                    [[sg.Text('Enter text to base64 encode it')],      
                     [sg.InputText(key='-IN-')],      
                     [sg.Submit(), sg.Cancel()]]).read(close=True)  

try:
    to_return = (values['-IN-']).encode("ascii")
    to_return = base64.b64encode(to_return)
    to_return = codecs.decode(to_return, 'UTF-8')
except ValueError:
    sg.popup("You didn't enter a number")
# finally show the input value in a popup window
sg.popup('Base64 Encoded', to_return)