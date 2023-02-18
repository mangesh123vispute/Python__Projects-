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

def health():
    engine.setProperty('rate', 160)
    command = 'nothing'
    while True:
        if __name__ == '__main__':

            notification.notify(
                title='**Take Break for 2 min**',
                message='Get up form desk afer each 1 hr ',
                app_icon=r"C:\Users\laxma\OneDrive\Desktop\public pro_jects\Python__Projects-\Reminder application for windows\exercise_cardio_running_treadmill_fitness_diet_icon_149037.ico",
                timeout=60)

        while (('done' not in command) and ('okay'not in command)):
            time.sleep(3)
            speak('sir, please take break , You must exercise after every 1 hour')
            command = takeCommands().lower()

        print("next one hr timer")
        command = 'nothing'
        time.sleep(60*60)

def NewCommandForApp():
    speak("Enter appname and command to open app and close app")
    speak("please note it is importent to give respective extention after commands,read below note for extention")
    print("\n\nExtensions for commands:\n.oa to open app\n.ca to close app\n.ow to open web\n.cw to close web\n.of to open file\n.cf to close file\n.ofd to open folder\n.cfd to close folder\nwrite .of,.cf etc after entering respective commands")
    print('\neg. whatsapp.oa  - open whatsapp\n whatsapp.ca - close whatsapp\n youtube.ow - open youtube\n youtube.cw - close youtube\n')
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
    speak("please note it is importent to give respective extention after commands,read below note for extention")
    print("\n\nExtensions for commands:\n.oa to open app\n.ca to close app\n.ow to open web\n.cw to close web\n.of to open file\n.cf to close file\n.ofd to open folder\n.cfd to close folder\nwrite .of,.cf etc after entering respective commands")
    print(
        '\neg. whatsapp.oa  - open whatsapp\n whatsapp.ca - close whatsapp\n youtube.ow - open youtube\n youtube.cw - close youtube\n')

    speak("Enter web url and command to open web ")
    url = input("Enter web url:\t")
    commando = input("Enter command to open web:\t")
    commandc = input("Enter command to close the web:\t")
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

    # code to wish user
    wishme()
    engine.setProperty('rate', 160)
    command = 1
    while command:
        query2 = 'none'
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            # Code for checking file exist
            try:
              
                

                file = __builtins__.open('cmd.txt', 'r')
                contain = file.read()
                length = len(contain)

                # if file dosent exist if folder

                if (length == 0):
                    choice = 1
                    while choice:
                        speak("Enter at list one command before moving forward")
                        print("1 for app\n2 for web\n3 for file")
                        choice = int(input())
                        if (choice == 1):
                            NewCommandForApp()
                            break
                        elif (choice == 2):
                            NewCommandForWeb()
                            break
                        elif (choice == 3):
                            NewCommandForFile()
                            break
                else:
                    print("Commands:")
                    print(
                        '--------------------------------------------------------------------------------------------------------------')
                    print(contain)
                    file.close()
                    print(
                        "NewAppcmd : to add new app command\nNewWebcmd : to new add web commands\nNewFilecmd: to add new file commands\nChangecmd: to change command\nNewFoldercmd: for new folder command\nexit :Exit the program")
                    print(
                        '--------------------------------------------------------------------------------------------------------------')
                    speak("please enter your command")
                    query2 = input("\nEnter your command:\n")

            except Exception as e:
                file = __builtins__.open('cmd.txt', 'a')
                file.close()
                print(e)

            # logic for command line

            if ('.oa' in query2.lower()):
                OpenApp()
            elif ('.of' in query2.lower()):
                OpenFile()
            elif ('.ow' in query2.lower()):
                OpenWeb()
            elif ('.ca' in query2.lower()):
                CloseApp()
            elif ('.cf' in query2.lower()):
                CloseFile()
            elif ('.cw' in query2.lower()):
                CloseWeb()
            elif('.ofd' in query2.lower()):
                OpenFolder()
            elif('.cfd' in query2.lower()):
                CloseFolder()
            elif ("NewWebcmd".lower() in query2.lower()):
                NewCommandForWeb()
            elif ("NewAppcmd".lower() in query2.lower()):
                NewCommandForApp()
            elif ("NewFilecmd".lower() in query2.lower()):
                NewCommandForFile()
            elif ("NewWebcmd".lower() in query2.lower()):
                NewCommandForWeb()
            elif("NewFoldercmd".lower() in query2.lower()):
                NewFoldercmd()
            

            elif ('exit' in query2):
                speak("good bye sir")
                sys.exit()

            else:
                speak("Enter correct command, Enter 1 to continue or 0 to discontinue")
                command = int(input("\n1 : To continue\n0 :To discontinue\n "))
                if (command == 0):
                    speak("good bye sir")
                    sys.exit()

        except Exception as e:
            speak("something went wrong,Enter 1 to continue or 0 to discontinue")
            print(e)
            command = int(input("\n1 : To continue\n0 :To discontinue\n "))
