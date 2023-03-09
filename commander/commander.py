import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyautogui
import time
import wikipedia
import os
import sys
import builtins
from AppOpener import open, close
import json
from plyer import notification
from selenium import webdriver
import subprocess

query2 = 'none'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hr = int(datetime.datetime.now().hour)
    if (hr >= 0 and hr < 12):
        speak("good morning,sir!")
    elif (hr >= 12 and hr < 18):
        speak("good afternoon,sir!")
    else:
        speak("good evening,sir!")

    speak("i am BumblebeeJarvis version 1.0.2 ")

def takeCommands():
    ''' It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 270
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said:{query}')

    except Exception as e:
        print('say that again please')
        return "None"
    return query



def NewCommandForApp():
    speak("Enter appname and command to open app and close app")
    appname = input("Enter appname: ")
    commando = (input("Enter command to open app:\t")).lower()
    commandc = (input("Enter command to close app:\t")).lower()
    while True:
        c = 1
        d = 1
        e = 1


        file = __builtins__.open('search.txt', 'a+')
        content = file.read()
        content = content.split(',')
        if appname in content:
            speak("Enter unique appname")
            print("Enter unique appname")
            appname = input("Enter appname: ")
            c = 0

        if commando in content or '.oa' not in commando:
            speak("Enter unique command to open app with .oa extention")
            commando = (
                input("Enter command to open app with .oa extention:\t")).lower()
            d = 0

        if commandc in content or '.ca' not in commandc:
            speak("Enter unique command to close app with extention .ca")
            commandc = (
                input("Enter command to close app with extention .ca:\t")).lower()
            e = 0

        if c == 1 and d == 1 and e == 1:
            file.close()
            break
    # writing in command file
    file = __builtins__.open('cmd.txt', 'a')
    dico = {commando: appname}
    dicc = {commandc: appname}
    dico = str(dico)
    dicc = str(dicc)
    file.write(dico + '\n')
    file.write(dicc + '\n')
    file.close()

    # writing in search file
    file = __builtins__.open('search.txt', 'a')
    cod = f"{appname},{commando},{commandc},"
    file.write(cod)
    file.close()



def NewCommandForWeb():

    speak("Enter web url and command to open web ")
    url = input("Enter web url:\t")
    commando = input("Enter command to open web:\t")
    commandc = input("Enter command to close the web:\t")
    commando=commando+'.ow'
    commandc=commandc+'.cw'
    while True:
        c = 1
        d = 1
        e = 1
        file = __builtins__.open('search.txt', 'r')
        content = file.read()
        content = content.split(',')
        if url in content:
            speak("Enter unique website url")
            print("Enter unique website url")
            url = input("Enter new url: ")
            c = 0

        if commando in content or '.ow' not in commando:
            speak("Enter unique command to open website with extention .ow")
            commando = (
                input("Enter command to open web with extention .ow:\t")).lower()
            d = 0

        if commandc in content or '.cw' not in commandc:
            speak("Enter unique command to close the website with extention .cw")
            commandc = (
                input("Enter command to close website with extention .cw:\t")).lower()
            e = 0

        if c == 1 and d == 1 and e == 1:
            file.close()
            break
    # writing in command file
    file = __builtins__.open('cmd.txt', 'a')
    dico = {commando: url}
    dicc = {commandc: url}
    dico = str(dico)
    dicc = str(dicc)
    file.write(dico + '\n')
    file.write(dicc + '\n')
    file.close()

    # writing in search file
    file = __builtins__.open('search.txt', 'a')
    cod = f"{url},{commando},{commandc},"
    file.write(cod)
    file.close()

def NewCommandForFile():
    speak("please note it is importent to give respective extention after commands,read below note for extention")
    print("\n\nExtensions for commands:\n.oa to open app\n.ca to close app\n.ow to open web\n.cw to close web\n.of to open file\n.cf to close file\n.ofd to open folder\n.cfd to close folder\nwrite .of,.cf etc after entering respective commands")
    print(
        '\neg. whatsapp.oa  - open whatsapp\n whatsapp.ca - close whatsapp\n youtube.ow - open youtube\n youtube.cw - close youtube\n')

    speak("Enter file path and command to open file and close file")
    path = input("Enter file path:\t")
    commando = input("Enter command to open file:\t")
    commandc = input("Enter command to close file:\t")

    while True:
        c = 1
        d = 1
        e = 1
        file = __builtins__.open('search.txt', 'r')
        content = file.read()
        content = content.split(',')
        if path in content:
            speak("Enter unique file path")
            print("Enter unique file path")
            path = input("Enter new path: ")
            c = 0

        if commando in content or '.of' not in commando:
            speak("Enter unique command to open file with command extention .of")
            commando = (
                input("Enter unique command to open file with command extention .of\t")).lower()
            d = 0

        if commandc in content or '.cf' not in commandc:
            speak("Enter unique command to close the file with command extention .cf")
            commandc = (input(
                "Enter unique command to close the file with command extention .cf\t")).lower()
            e = 0

        if c == 1 and d == 1 and e == 1:
            file.close()
            break
    # writing in command file
    file = __builtins__.open('cmd.txt', 'a')
    dico = {commando: path}
    dicc = {commandc: path}
    dico = str(dico)
    dicc = str(dicc)
    file.write(dico + '\n')
    file.write(dicc + '\n')
    file.close()

    # writing in search file
    file = __builtins__.open('search.txt', 'a')
    cod = f"{path},{commando},{commandc},"
    file.write(cod)
    file.close()

def NewCommandForFolder():
    speak("Enter folder path and command to open folder and close folder")
    speak("please note it is importent to give respective extention after commands,read below note for extention")
    print("\n\nExtensions for commands:\n.oa to open app\n.ca to close app\n.ow to open web\n.cw to close web\n.of to open file\n.cf to close file\n.ofd to open folder\n.cfd to close folder\nwrite .of,.cf etc after entering respective commands")
    print('\neg. whatsapp.oa  - open whatsapp\n whatsapp.ca - close whatsapp\n youtube.ow - open youtube\n youtube.cw - close youtube\n')
    folderpath=input("Enter folder path:\t")
    commando = (input("Enter command to open folder:\t")).lower()
    commandc = (input("Enter command to close folder:\t")).lower()
    while True:
        c = 1
        d = 1
        e = 1

        file = __builtins__.open('search.txt', 'a+')
        content = file.read()
        content = content.split(',')
        if folderpath in content:
            speak("Enter unique folder path ")
            print("Enter unique folder path")
            folderpath = input("Enter folderpath: ")
            c = 0

        if commando in content or '.ofd' not in commando:
            speak("Enter unique command to open folder with .ofd extention")
            commando = (
                input("Enter command to open folder with .ofd extention:\t")).lower()
            d = 0

        if commandc in content or '.cfd' not in commandc:
            speak("Enter unique command to close folder with extention .cfd")
            commandc = (
                input("Enter command to close folder with extention .cfd:\t")).lower()
            e = 0

        if c == 1 and d == 1 and e == 1:
            file.close()
            break
    # writing in command file
    file = __builtins__.open('cmd.txt', 'a')
    dico = {commando: folderpath}
    dicc = {commandc: folderpath}
    dico = str(dico)
    dicc = str(dicc)
    file.write(dico + '\n')
    file.write(dicc + '\n')
    file.close()

    # writing in search file
    file = __builtins__.open('search.txt', 'a')
    cod = f"{folderpath},{commando},{commandc},"
    file.write(cod)
    file.close()



def OpenApp():
    # program to fetch command form the file  and opening app
    command = query2
    commandline = 'none'
    content = True
    i = 0
    file = __builtins__.open('cmd.txt', 'r')
    while (content):
        content = file.readline()
        if (command.lower() in content.lower()):
            commandline = eval(content)
            open(commandline[command])
            i = 1
            file.close()
            break
    if (i == 0):
        speak("No command found, please retry")

def OpenFolder():
    # program to fetch command form the file  and opening folder
    command = query2
    commandline = 'none'
    content = True
    i = 0
    file = __builtins__.open('cmd.txt', 'r')
    while (content):
        content = file.readline()
        if (command.lower() in content.lower()):
            commandline = eval(content)
            os.startfile(commandline[command])
            i = 1
            file.close()
            break
    if (i == 0):
        speak("No command found, please retry")

def OpenFile():
    command = query2
    commandline = 'none'
    content = True
    i = 0
    file = __builtins__.open('cmd.txt', 'r')
    while (content):
        content = file.readline()
        if (command in content.lower()):
            commandline = eval(content)
            os.startfile(commandline[command])
            i = 1
            file.close()
            break

    if (i == 0):
        speak("No command found , please retry")

def OpenWeb():
    command = query2
    commandline = 'none'
    content = True

    file = __builtins__.open('cmd.txt', 'r')
    while (content):
        content = file.readline()
        if (command.lower() in content.lower()):
            commandline = eval(content)
            webbrowser.open(commandline[command])
            file.close()

def CloseApp():
    command = query2
    commandline = 'none'
    content = True

    file = __builtins__.open('cmd.txt', 'r')
    while (content):
        content = file.readline()
        if (command.lower() in content.lower()):
            commandline = eval(content)
            close(commandline[command])
            file.close()
            break

def CloseWeb():
    pyautogui.hotkey('ctrl', 'w')
    speak("go to web page and hit control plus w to close the current website")
    print("1.Go to web page\n2.hit ctrl+w  to close the current website")

def CloseFile():
    speak("sir ,you have to close file manually due to some technical issue")

def ChangeCommand():
    pass

# NewCommandForFolder()
def deletecommand():
    pass


if __name__ == "__main__":
    Input=[]
    # code to wish user
    startTime=time.time()
    wishme()
    engine.setProperty('rate', 160)
    command = 1
    while command:
        query2 = 'none'
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            speak("How can i help you sir, please tell your commands")



            if ('.oa' in query2.lower()):
                OpenApp()
                Input.append(1)
            elif ('.of' in query2.lower()):
                OpenFile()
                Input.append(1)
            elif ('.ow' in query2.lower()):
                OpenWeb()
                Input.append(1)
            elif ('.ca' in query2.lower()):
                CloseApp()
                Input.append(1)
            elif ('.cf' in query2.lower()):
                CloseFile()
                Input.append(1)
            elif ('.cw' in query2.lower()):
                CloseWeb()
                Input.append(1)
            elif('.ofd' in query2.lower()):
                OpenFolder()
                Input.append(1)
            elif('.cfd' in query2.lower()):
                CloseFolder()
                Input.append(1)
            elif ("NewWebcmd".lower() in query2.lower()):
                NewCommandForWeb()
                Input.append(1)
            elif ("NewAppcmd".lower() in query2.lower()):
                NewCommandForApp()
                Input.append(1)
            elif ("NewFilecmd".lower() in query2.lower()):
                NewCommandForFile()
                Input.append(1)
            elif ("NewWebcmd".lower() in query2.lower()):
                NewCommandForWeb()
                Input.append(1)
            elif("NewFoldercmd".lower() in query2.lower()):
                NewFoldercmd()
                Input.append(1)
            elif ('exit' in query2):
                speak("good bye sir")
                sys.exit()
                Input.append(1)
            if(time.time()-startTime)>=900:
                speak("sir do you want to continue the program,speak yes to continue else speak no to exit")

            else:
                cd='none'
                speak("call my name if you want my assistance,else speak exit to exit the program")
                while 'jarvis' not in cd and 'exit' not in cd:
                    Input.append(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cd=''
                    cd=takeCommands().lower()
                if ('exit' in cd):
                    Input.append(1)
                    speak("good bye sir")
                    sys.exit()

        except Exception as e:
            speak("something went wrong,Enter 1 to continue or 0 to discontinue")
            print(e)
            command = int(input("\n1 : To continue\n0 :To discontinue\n "))
