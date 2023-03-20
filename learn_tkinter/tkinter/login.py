from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login") # -> title from box
root.geometry("200x100") # -> size of box

username = "angga"
password = "angga123"

def login():
    user = e1.get()
    pas = e2.get()

    # massagebox: showinfo, showwarning, showeror, askqustion, askokcancel, askyesno
    if(username == user and password == pas):
        messagebox.showinfo("Admin place ", " Cograts you sucses to login")
    else:
        messagebox.showwarning("Error", "Sorry you password or username is wrong")


# make label
label = Label(root, text="Login admin")
label.pack()

# make entry or input
e1 = Entry(root)
e1.pack()
e1.insert(1, "Username...") # -> must enter string and index(0)

e2 = Entry(root)
e2.pack()
e2.insert(0, "Password...")

# make button in tkinter
button = Button(root, text="Login", command=login)
button.pack()

root.mainloop()