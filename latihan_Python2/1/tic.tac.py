from typing import DefaultDict


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '7': ' ', '8': ' ', '9': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_key = []

for key in theBoard:
    board_key.append(key)

def printBoard (board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    
def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("it's ", turn, " turn \Please which one place")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("This place as already filled \nPlease which difrent place")
            continue

        if count == 5:
            if theBoard == ['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break
            
            elif theBoard == ['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break

            elif theBoard == ['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break

            elif theBoard == ['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break

            elif theBoard == ['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break

            elif theBoard == ['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break

            elif theBoard == ['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break

            elif theBoard == ['1'] == theBoard['2'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(turn, "WIN")
                break

        if count == 9:
            print("It's Tie no Winner")
    
    restart = input ("Do you want to restart the game (y/n) ")
    if restart == 'Y' or restart == 'y':
        for key in board_key:
            theBoard[key] = ' '
        game()

if __name__ == "__main__":
    game()
print("Good Bye")



