from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk

window = Tk()
window. title("Sign UP")
window.geometry('925x500+300+200')
window.configure(bg = '#fff')
window.resizable(False, False)

img = Image.open("C:\Users\edwar\Music\My Code\python\TKINTER\signUp\Login.jpg")
imaga = ImageTk.PhotoImage(img)
Label(window,image=img,border=0, bg='white').place(x=50, y=90)


# img =  PhotoImage(file='Login.jpg')
# 

frame = Frame(window,width=350, height=390, bg='red')
frame.place(x=480, y=50)



window.mainloop()