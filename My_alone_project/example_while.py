# make name line-up use python
user = 0
while user != 9:
    user = int(input("enter you player = "))

    player = ['kuroko', 'kagami ', 'hyuga ', 'teppei ', 'roony', 'rossi']

    if 1 <= user <= 7:
        print("Name player = ", player[user - 1])
