import time
from plyer import notification
if __name__ == '__main__':
        while True:
                notification.notify(
                        title='**Take Break for 2 min**',
                        message='Get up form desk afer each 1 hr ',
                        app_icon=r"C:\Users\laxma\OneDrive\Desktop\public pro_jects\Python__Projects-\Reminder application for windows\exercise.ico",
                        timeout=15
                )
                time.sleep(5)


