# setiap kelas di python menggunkan huruf besr

import tkinter

main_window = tkinter.Tk()

def lat():
    label5 = tkinter.Label(main_window, text="This text in window")
    print("This text in terminal")
    label5.pack()

label1 = tkinter.Label(main_window, text="This is example")
label2 = tkinter.Label(main_window, text="This is example2")
label3 = tkinter.Label(main_window, text="This is example3")

tombol = tkinter.Button(main_window, text="This is Button", command=lat)


label1.pack()
label2.pack()
label3.pack()
tombol.pack()



main_window.mainloop()
