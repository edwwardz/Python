from tkinter import *

root = Tk()
root.title("First")

color = ['red','white','blue','cyan','yellow','purple']


r = 0
for item in color:
    Label(text=item, relief=RIDGE, width=15).grid(row=r,column=0)
    Entry(bg=item, relief=RIDGE, width=10).grid(row=r,column=1)
    r = r + 1

root.mainloop()

#Description:
"""Fungction:
Relief = membuat tampilan text menjadi semakin bagus
Width = Mengatur lebar text
"""