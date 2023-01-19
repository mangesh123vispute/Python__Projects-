import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import time
import sys
from AppOpener import open,close


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

    speak("i am BumblebeeJarvis version 1.0.2 . Please tell me how may i help you ! ")


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


if __name__ == "__main__":
    
    wishme()
    engine.setProperty('rate', 160)
    i = 0
    condition = True
    while (condition):
        os.system('cls' if os.name == 'nt' else 'clear')
        if (i != 0 and i != 3):
            speak('How can i help you sir')

        try:
            query = takeCommands().lower()
            i = 1

            # logic for execution task based on query
            if ('wikipedia' in query):
                query = query.replace('wikipedia', '')
                result = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(result)
                speak(result)
                speak("sir, what is my next command")
                i=0

            elif ("youtube" in query):
                webbrowser.open("youtube.com")
                speak("sir, what is my next command")
                i=0
            elif ("google" in query):
                webbrowser.open("google.com")
                speak("sir, what is my next command")
                i=0
            elif (" stack overflow" in query):
                webbrowser.open("stackoverflow.com")
                speak("sir, what is my next command")
                i=0
            elif ("the time" in query):
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak(f"Sir, The time is {strTime}")
                speak("sir, what is my next command")
                i=0
            elif (('open vs code' and 'practice' in query) or ('open vs code') in query):
                os.startfile(
                    "C:\\Users\\laxma\\OneDrive\\Desktop\\dsa and practice\\file_opening.cpp")
                speak("sir, what is my next command")
                i=0
            elif ('open vs code' and 'project' in query):
                os.startfile(
                    "C:\\Users\\laxma\\OneDrive\\Desktop\\public pro_jects\\project.cpp")
                speak("sir, what is my next command")
                i=0
            
            elif (('microsoft' in query) and ('open' in query)):
                    open("Microsoft Edge")
                    speak("sir, what is my next command")
                    i=0
            elif (('microsoft' in query) and ('close' in query) ):
                    close("Microsoft Edge")
                    speak("sir, what is my next command")
                    i=0
            elif (('whatsapp' in query) and ('open' in query)):
                    open("whatsapp")
                    speak("sir, what is my next command")
                    i=0
            elif (('close' in query) and ('whatsapp' in query)):
                close("whatsapp")
                speak("sir, what is my next command")
                i = 0
            elif (('python' in query) and ('open' in query)):
                    open("PyCharm")
                    speak("sir, what is my next command")
                    i=0

            elif (('store' in query) and ('open' in query)):
                    open("GitHub Desktop")
                    speak("sir, what is my next command")
                    i=0
            
            
            elif (('hold' in query) or ("wait" in query)):
                speak("Enter jarvis if you want my assistance ")
                condition=False
                while(condition==False):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("jarvis==continue\nexit==close\n")
        
                    command=input("Enter your command\n")
                    if(command=='jarvis'):
                        condition = True
                        speak("welcome back sir, ") 
                    elif(command=='exit'):
                        condition = False
                        speak("good bye sir")
                        sys.exit()
                    else:
                        print("Enter valid command\n")
                        condition = False
                
                    

                    
            elif ('exit' in query):
                speak("good bye sir")
                sys.exit()
                

            else:
                time.sleep(5)
                speak("sir, what is your next command ")
                i = 0

        except Exception as e:
            print(e)
            speak("sorry sir ,may you please repeat ")
            i = 3
