from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob

root = Tk()
root.title("Google Translate")
root.geometry("1080x400")

language=googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combol = ttk.Combobox(root,values=languageV,font="Roboto 14", state='r')
combol.place(x=110, y=20)
combol.set("ENGLISH")

Label1 = Label(root,text="English",font="segoe 30 bold", bg='white', width=18, bd=5, relief=GROOVE)
Label1.place(x=10, y=50)

f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f,font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0,y=0,width=430, height=200)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side="right", fill='y')

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)


combo2 = ttk.Combobox(root,values=languageV,font="RobotV 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

Label2 = Label(root,text="English",font="segoe 30 bold", bg='white', width=18, bd=5, relief=GROOVE)
Label2.place(x=620, y=50)


root.configure(bg="white")
root.mainloop()