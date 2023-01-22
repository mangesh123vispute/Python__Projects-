import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import time
import sys
from AppOpener import open,close
from plyer import notification


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
    command='nothing'
    while True:
        if __name__ == '__main__':

                notification.notify(
                        title='**Take Break for 2 min**',
                        message='Get up form desk afer each 1 hr ',
                        app_icon=r"C:\Users\laxma\OneDrive\Desktop\public pro_jects\Python__Projects-\Reminder application for windows\exercise_cardio_running_treadmill_fitness_diet_icon_149037.ico",
                        timeout=60)
       
        while(('done' not in command) and ('okay'not in command) ):
                time.sleep(3)
                speak('sir, please take break , You must exercise after every 1 hour')
                command=takeCommands().lower()
              
        print("next one hr timer")
        command='nothing'
        time.sleep(60*60)




if __name__ == "__main__":
    # health()
    wishme()
    engine.setProperty('rate', 160)
    query='none'
    query2='none'
    i = 0
    mode=3
    speak('Enter mode:')
    while(mode!=1 and mode!=2):
        try:
            mode = int(input("1.speaking\n2.command line\n"))
            if(mode==1):
                speak("speaking mode is on")
            elif(mode==2):
                speak("command mode is on")
        except Exception as e:
            print(e)
            speak('enter valid command')

    condition = True
    while (condition):
        query='none'
        query2='none'
        os.system('cls' if os.name == 'nt' else 'clear')
        if (i != 0 and i != 3):
            speak('How can i help you sir')

        try:
            if(mode==1):
                speak('tell your commands')
                query = takeCommands().lower()
            elif(mode==2):
                print("\ncommands\n1.wikipedia==<search> wikipedia\n2.open youtube=youtube\n3.open google=google\n4.open stackoverfolw=stack\n"
                      "5.current time=time\n6.open vs code in  practice= vs code pra\n"
                      "7.open vs code in project= vs code pro\n8.open microsoft edge=micro\n9.close microsoft edge=microc\n10.open whatsapp= whatsappo\n11.close whatsapp=whatsappc\n12.open github='githubo\n"
                      "13.hold the program= hold/wait\n14.exit=exit\n15.close github= githubc\n16.switch mode:speaking mode=mode1,command mode=mode2"
                      "")
                speak("Enter your commands")
                query2=input("\nEnter your command:\n")

            i = 1

            # logic for execution task based on query
            if (('wikipedia' in query)or (query2=='wikipedia')):
                query = query.replace('wikipedia', '')
                result = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(result)
                speak(result)
                speak("press j to continue")
                condition=input('Enter command')
                i=0

            elif (("youtube" in query) or (query2=='youtube')):
                webbrowser.open("youtube.com")
                speak("press j to continue")
                condition=input('Enter command')
                i=0
            elif (("google" in query)or(query2=='google')):
                webbrowser.open("google.com")
                speak("press j to continue")
                condition=input('Enter command')
                i=0
            elif (("stack" in query)or(query2=='stack')):
                webbrowser.open("stackoverflow.com")
                speak("press j to continue")
                condition=input('Enter command')
                i=0
            elif (("time" in query)or(query2=='time')):
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak(f"Sir, The time is {strTime}")
                speak("press j to continue")
                condition=input('Enter command')
                i=0
            elif ((('vs code ' in query) and ('practice' in query) )or (query2=='vs code pra')):
                os.startfile(
                    "C:\\Users\\laxma\\OneDrive\\Desktop\\dsa and practice\\file_opening.cpp")
                speak("press j to continue")
                condition=input('Enter command')
                i=0
            elif ((('vs code ' in query) and ('project' in query) )or (query2=='vs code pro')):
                os.startfile(
                    "C:\\Users\\laxma\\OneDrive\\Desktop\\public pro_jects\\project.cpp")
                speak("press j to continue")
                condition=input('Enter command')
                i=0
            
            elif ((('microsoft' in query) and ('open' in query))or (query2=='micro')):
                    open("Microsoft Edge")
                    speak("press j to continue")
                    condition=input('Enter command')
                    i=0
            elif ((('microsoft' in query) and ('close' in query)) or (query2=='microc')):
                    close("Microsoft Edge")
                    speak("press j to continue")
                    condition=input('Enter command')
                    i=0
            elif ((('whatsapp' in query) and ('open' in query)) or (query2=='whatsappo')):
                    open("whatsapp")
                    speak("press j to continue")
                    condition=input('Enter command')
                    i=0
            elif ((('close' in query) and ('whatsapp' in query))or(query2=='whatsappc')):
                close("whatsapp")
                speak("press j to continue")
                condition=input('Enter command')
                i = 0
            elif (('python' in query) and ('open' in query)):
                    open("pycharm64")
                    speak("press j to continue")
                    condition=input('Enter command')
                    i=0

            elif ((('store' in query) and ('open' in query))or (query2=='githubo')):
                    open("GitHub Desktop")
                    speak("press j to continue")
                    condition=input('Enter command')
                    i=0
            elif ((('store' in query) and ('close' in query))or (query2=='githubc')):
                    close("GitHub Desktop")
                    speak("press j to continue")
                    condition=input('Enter command')
                    i=0
                    
            elif (('exit' in query) or (query2=='exit')):
                speak("good bye sir")
                sys.exit()
            elif((query2=='mode1') or ('speaking mode' in query )):
                speak("speaking mode is on ")
                speak("press j to continue")
                condition=input('Enter command')
                mode=1

            elif ((query2 == 'mode2') or ('command mode' in query)):
                speak("command mode is on ")
                speak("press j to continue")
                condition=input('Enter command')
                mode = 2


            else:
                time.sleep(5)
                speak("sir, what is your next command ")
                i = 0

        except Exception as e:
            print(e)
            speak("sorry sir ,may you please repeat ")
            i = 3
