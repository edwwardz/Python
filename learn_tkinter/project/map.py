import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#><|\/$%^&*()_+(')"

while 1:
    password_len = int(input("What lenght would you like you password to be : " ))
    password_count = int(input("How many password would you like: "))
    for x in range(0,password_count):
        password = ""
        for x in range(password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here Is you password: ", password)
            