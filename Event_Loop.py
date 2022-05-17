import PySimpleGUI as sg
import base64
import codecs
import urllib.parse

sg.theme('Dark Amber')

#Layout

layout = [
    [sg.Text("Enter a string into one of the inputs")],
    [sg.Text("Base64 Encoder", size=(13,1)),sg.Input(key= '-B64-'), sg.Button("Encode", key="OnlyBase64")],
    [sg.Text("URL Encoder", size=(13,1)),sg.Input(key='-URL-'), sg.Button("Encode", key="OnlyURL") ],
    [sg.Button("Calculate Both", expand_x=True, key='Enter'), sg.Button("Exit", expand_x=True)]
]

#Open window
window = sg.Window("Encoder/Decoder", layout, return_keyboard_events=True)

''' Helper Functions'''

#Take in a string and Base64 Encode it. Return a string
def Base64(value:str)-> str :
    value = base64.b64encode(value.encode("ascii"))
    value = codecs.decode(value, "UTF-8")
    return value

def URLEncode(value:str)->str:
    value = urllib.parse.quote(value)
    return value

#Event Loop
while True:
    event, value = window.read()
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == 'Enter':
        sg.popup("Base64: ", Base64(value['-B64-']), "\nURL: ", URLEncode(value['-URL-']))
    if event == "OnlyBase64":
        sg.popup("You hit the base64 button ", Base64(value['-B64-']))
    if event == "OnlyURL":
        sg.popup("You hit the URL button ", URLEncode(value['-URL-']))
window.close()