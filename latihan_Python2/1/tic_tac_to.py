theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_key = []

for key in theBoard:
    board_key.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('_+_+_')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('_+_+_')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
        
def game():

    turn = 'X'
    count = 0
    
    for i in range(10):
        printBoard(theBoard)
        print("It's you turn " + turn + " Please which one place")
        
        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("This place already filled \nPlease which one place")
            continue

        if count >= 5:
            if theBoard ['7'] == theBoard ['8'] == theBoard ['9'] != ' ' :
                printBoard(theBoard)
                print("Game over")
                print("Congrats " + turn+ " You win")
                break

            if theBoard ['3'] == theBoard ['6'] == theBoard ['9'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Congrats "+ turn+ " You win")
                break

            if theBoard ['1'] == theBoard ['2'] == theBoard ['3'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Congrats "+ turn+ " You win")
                break        
            
            if theBoard ['1'] == theBoard ['4'] == theBoard ['7'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Congrats "+ turn+ " You win")
                break

            if theBoard ['4'] == theBoard ['5'] == theBoard ['6'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Congrats "+ turn+ " You win")
                break
            
            if theBoard ['2'] == theBoard ['5'] == theBoard ['8'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Congrats "+ turn+ " You win")
                break
            
            if theBoard ['7'] == theBoard ['5'] == theBoard ['3'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Congrats "+ turn+ " You win")
                break            
            
            if theBoard ['1'] == theBoard ['2'] == theBoard ['9'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Congrats "+ turn + " You win")
                break

        if count == 9:
            print("Not winner \n")
            print("It's Tie")
        
        if turn == 'X':
            turn ='O'
        else:
            turn = 'X'

    restart = input("Do you want to reset the game (y/n) = ")
    if restart == "y" or restart == "Y":
        for key in theBoard:
            theBoard[key] = " "
        game()

if __name__ == '__main__':
    game()
print("Good Bye")

        