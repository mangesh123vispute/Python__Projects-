import time
import Jarvis
import pyttsx3
from plyer import notification

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)
command='nothing'


while True:
        if __name__ == '__main__':

                notification.notify(
                        title='**Take Break for 2 min**',
                        message='Get up form desk afer each 1 hr ',
                        app_icon=r"C:\Users\laxma\OneDrive\Desktop\public pro_jects\Python__Projects-\Reminder application for windows\exercise_cardio_running_treadmill_fitness_diet_icon_149037.ico",
                        timeout=60)
       
        while(('Done' not in command) and ('okay'not in command) ):
                time.sleep(3)
                Jarvis.speak('sir, please take break , You must exercise after every 1 hour')
                command=Jarvis.takeCommands()
              
        print("next one hr timer")
        command='nothing'
        time.sleep(60*60)


                
        
                
        
        
                

         
              
                


