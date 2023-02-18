import time
import pyttsx3
from plyer import notification
import os
import ctypes
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

def check():
        start_time = time.time()
        end_time = time.time()
        Time = end_time - start_time
        ctypes.windll.user32.LockWorkStation()

        while Time <=60 :
                Time = time.time() - start_time
                if (Time < 60 ):
                        ctypes.windll.user32.LockWorkStation()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


command=True
count=False
while True:
        if count:
                notification.notify(
                        title='**Take Break for 2 min**',
                        message='Get up form desk afer each 1 hr ',
                        app_icon=r"C:\Users\laxma\OneDrive\Desktop\public pro_jects\Python__Projects-\Reminder application for windows\exercise_cardio_running_treadmill_fitness_diet_icon_149037.ico",
                        timeout=60)
                speak("sir, please take break for 1 min and exercise")
                check()
        speak("one hour timer is set")
        time.sleep(60*60)
        count = True







                
        
                
        
        
                

         
              
                


