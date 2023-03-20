menu = 0
test = {250706, 101114, 231176}

while menu < 3:
    print ("Hello everybody")
    print ("How are you")
    print ("Welcome to last test in school")
    print ("To start the test please enter you name and you token")
    print ("1. See my token")
    print ("2. Start test")
    menu = int(input("enter you option = "))
    
if menu == 1:
    name = input ("enter you name = ")
    if name == 'angga' or name == 'Angga':
        print ("You Token is 250706")
        test.append(name)
    elif name == 'castellani' or name == 'Castellani':
        print ("your number token is 101114" )
        test.append(name)
    elif name == 'budi' or name == 'Budi':
        print ("your number token is 231076")
        test.append(name)
    else:
        print ("sorry your name not found")


    
