#permainan tebak angka 
number = 13
guess = -1

print("Tebak number>........")
while guess != number:
    guess = int(input("get in the number = "))

    if guess == number:
        print("Congratulation you right ")
    elif guess < number:
        print("Angkanya lebih dari ", guess)
    elif guess > number:
        print ("Angkanya kurang dari ", guess)
