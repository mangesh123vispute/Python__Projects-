import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import time
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)


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
    i = 0
    condition = True
    while (condition):
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

            elif ("open youtube" in query):
                webbrowser.open("youtube.com")
                speak("sir, what is my next command")
                i=0
            elif ("open google" in query):
                webbrowser.open("google.com")
                speak("sir, what is my next command")
                i=0
            elif ("open stack overflow" in query):
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
            elif (('hold' in query) or ("wait") in query):
                speak("call my name if you what my assistance")
                condition = False
                while (condition == False):
                    newcommand = takeCommands().lower()
                    if ('exit' in newcommand):
                         speak("good bye sir")
                         sys.exit()
                         

                    if ('jarvis' in newcommand):
                        condition = True
                        speak("welcome back sir")

                    else:
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
