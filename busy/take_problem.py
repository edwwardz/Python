try :
    number = int(input("enter the number in 10 to 20 = "))
except ValueError:
        print("you must enter the number in 10 to 20! ")
else:
        if (number >= 10) and (number <= 20):
            print("the number you input is = ", number)
        else:
            print("You enter number more big/little for 10 to 20")