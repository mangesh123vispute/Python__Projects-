
from socket import SO_ACCEPTCONN
import pyttsx3
from plyer import notification
import os
import ctypes
import time
import subprocess
import plyer.platforms
import keyboard
from pynput import keyboard, mouse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

countdown_duration=0
relax=0
flag=0
start=0
countdown_started=0
countdown_time=0
time_spent=0
sp=False

def space():
    def handle_key_press(key):
        global sp
        if key == keyboard.Key.space:
            print("Space is pressed")
            sp=True
            return False

    with keyboard.Listener(on_press=handle_key_press) as listener:
           listener.join()


def searchword():
    global sp
    # get the absolute path to the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # the file containing words to be searched
    words_file = os.path.join(script_dir, "word.txt")
      
    # the file containing the index
    index_file = os.path.join(script_dir, "index.txt")

    # it this file words to be searched are stored
    with open(words_file,'a+') as f:
        f.seek(0)
        if not f.read():
                f.write("sandeep")
        f.seek(0)
        content = f.read()
        content = content.split('\n')

    # i is the index for content(words) list, initially 0
    
    with open(index_file,'a+') as f:
        f.seek(0)
        if not f.read():
                f.write('0')
        else:
                f.seek(0)
                i=int(f.read())
        
    try:
             # Create an instance of Chrome WebDriver
                driver = webdriver.Chrome()
                # Navigate to Google website
                driver.get("https://www.google.com/")
                # Find the search bar and enter the word
                search_bar = driver.find_element(by='name', value='q')
                # suppose if index is grater than words then we reset it to 0th index to repeat same set of words
                if i>len(content)-1:
                    i=0
                    with open(index_file,'w') as f:
                            f.write('0')
                # searching word at index i
                search_bar.send_keys(f"{content[i]}")
                # incrementing word index by one
                i += 1
                # storing it to file
                with open(index_file,'w') as f:
                    f.write(str(i))
                search_bar.send_keys(Keys.RETURN)

                #    below code will test space is pressed or not ,if pressed then it will close microsoft edge
                speak("press space to exit browser")
                while sp==False:
                    space() 

                sp=False 
                driver.quit()
    except Exception as e:
                print(e)
                
    

def check2(): 
        global start
        global flag
        t=time.time()
        while start!=1 or flag!=1:
                checkactivity()
                T=time.time()
                if(T-t)>=600:                  #600 sec mins 10 min
                        speak("sir, are you using laptop")
                        speak("press 1 to continue reminder app, else press 0 ")
                        pressedornot=int(input("press 1 to continue reminder app, else press 0"))
                        if(pressedornot==0):
                                speak("Good bye ,sir")
                                sys.exit()
                        elif(pressedornot==1):
                                start=1
                                flag=1
def on_press(key):
    global flag
    global start
    global pressedornot
    # Handle key press event here
    flag = 1
    start = 1
def on_release(key):
    global flag
    global start
    # Handle key release event here
    flag = 1
    start = 1
def on_click(x, y, button, pressed):
        global flag
        global start
        # Handle mouse click event here
        flag=1
        start=1
def on_move(x, y):
        # Handle mouse move event here
        pass
def checkactivity():
        # Create listener objects for keyboard and mouse events
        keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)

        # Start the listener threads
        keyboard_listener.start()
        mouse_listener.start()

        time.sleep(10)

        # Stop the listener threads
        keyboard_listener.stop()
        mouse_listener.stop()

        # Block until the listener threads are finished
        keyboard_listener.join()
        mouse_listener.join()

# this function will check user is entering into laptop in the duration of break , if he is intering then again lock the screen till break duration overs
def check():
        global relax
        start_time = time.time()
        end_time = time.time()
        Time = end_time - start_time
        subprocess.call(['rundll32.exe', 'user32.dll,LockWorkStation'])
        while Time <=relax:
                Time = time.time() - start_time
                if (Time <relax ):
                        subprocess.call(['rundll32.exe', 'user32.dll,LockWorkStation'])
# this is count down 
def countdown():
        global countdown_duration
        global countdown_started
        global countdown_time
        global time_spent
        last_word_time=time.time()
        fsearchtime=0
        lsearchtime=0

    
        for remaining_time in range(countdown_duration, 0, -1):
                time_spent=time.time()-countdown_started           
                os.system('cls' if os.name == 'nt' else 'clear')
                minutes, seconds = divmod(remaining_time, 60)
                print(f"Countdown: {minutes:02d}:{seconds:02d}\n")
                countdown_str = f'Get up from the chair after {minutes:02d}:{seconds:02d} and move, exercise stretch for one to two minutes.'
                print(countdown_str, end='\r')  
                word_time=time.time()-last_word_time
                time.sleep(1)
                if word_time>=5:                
                        searchword()
                        last_word_time=time.time()
               

def main():
        global countdown_duration
        global relax
        global flag
        global start
        global countdown_started
        command=True
        count=False
        speak("Enter countdown duration in seconds")
        countdown_duration=int(input("\nEnter countdown duration in seconds:\nno. of sec=60*no. of min\t"))
        speak("Enter break duration")
        relax=int(input("\nEnter break duration in seconds:\t"))

        while start:
                if count:
                        notification.notify(
                                title=f'**Take Break for {int(relax/60)} min**',
                                message='Get up form desk afer each 1 hr ',
                                app_icon=r"C:\Users\laxma\OneDrive\Desktop\public pro_jects\Python__Projects-\reminder\exercise_cardio_running_treadmill_fitness_diet_icon_149037 (1).ico",
                                timeout=60)
                        speak(f"sir, please take break for {int(relax/60)} min and exercise")
                        check()
                        time.sleep(5)
                        check2()
                if flag==1:

                        speak(f"{int(countdown_duration/60)} minute timer is set")
                        countdown_started=time.time()
                        # This will search word before and after countdown
                        countdown()
                        flag=0
                        count = True
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



try:    
        check2()
        main()
except Exception as e:
        print(e)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
        







                
        
                
        
        
                

         
              
                


