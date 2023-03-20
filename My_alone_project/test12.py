menu = 0
test = 250706, 101114, 231176

while menu < 3:
    print ("Hello everybody")
    print ("How are you")
    print ("Welcome to last test in school")
    print ("To start the test please enter you name and you token")
    print ("1. See my token")
    print ("2. Start test")
    menu = int(input("enter you option = "))
    
if menu == 1:
   def name (name, token):
       print ("Hallo", name, "ini nomor token mu ya", token)
    name('angga', 250706)
    name("Castellani", 101114)
    name("Budi", 231176)


#elif menu == 2:
    #token = int(input("Enter you token"))
    #if token in test:
        #print ("Okay you can start the test")

