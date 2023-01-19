import tkinter
import cv2
import PIL.Image, PIL.ImageTk

# width and hight of our main screen
SET_WIDTH=650
SET_HEIGHT=368


# tkinter gui starts here
windows=tkinter.Tk()
windows.title("Third umpire decision kit")
cv_img=cv2.cvtColor(cv2.imread('welcome.png'),cv2.)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
canvas=tkinter.Canvas(windows,height=SET_HEIGHT,width=SET_WIDTH)
windows.mainloop()