import tkinter

window = tkinter.Tk()

def train ():
    label3 = tkinter.Label(window, text="Welcome to the online market ")
    label4 = tkinter.Label(window, text="This is the list:")
    label5 = tkinter.Label(window, text="1. Snack")
    label6 = tkinter.Label(window, text="2. Drink")
    label3.pack()
    label4.pack()
    label5.pack()
    label6.pack()

def snack ():
    var = input("You want to buy snack right y/n = ")
    if var == 'Y' or 'y':
        print("Okay you transaction process")
    elif var == 'N' or 'n':
        print ("Okay see you")
    
def drink ():
    var = input("You want to buy drink right y/n = ")
    if var == 'Y' or 'y':
        print("Okay you transaction process")
    elif var == 'N' or 'n':
        print ("Okay see you")
    
    
label = tkinter.Label(window, text="Hello welcome to the online market")

label2 = tkinter.Label(window, text="if you want to buy in the online market please enter the button")

button = tkinter.Button(window, text="Please press me", command= train)

label7 = tkinter.Label(window, text="\n")

snack = tkinter.Button(window, text= "Press me if you want to snack", command= snack)
    
drink = tkinter.Button(window, text="Press me if you want to buy Drink", command= drink)
    

label.pack()
label2.pack()
button.pack()
snack.pack()
drink.pack()
label7.pack()


window.mainloop()