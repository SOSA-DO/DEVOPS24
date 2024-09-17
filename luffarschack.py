theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])




def checkWinner(board):
    # Definiera alla vinnande kombinationer
    win_combinations = [
        ['1', '2', '3'], # rad 1
        ['4', '5', '6'], # rad 2
        ['7', '8', '9'], # rad 3
        ['1', '4', '7'], # kolumn 1
        ['2', '5', '8'], # kolumn 2
        ['3', '6', '9'], # kolumn 3
        ['1', '5', '9'], # diagonal 1
        ['3', '5', '7']  # diagonal 2
    ]

    # Kolla om någon av dessa kombinationer är fyllda med samma tecken
    for combo in win_combinations:

        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]] # Returnera vinnaren ('X' eller 'O')
    


turn = 'X'
for i in range(9):

    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()

    if move in theBoard.keys():
        if theBoard[move] == ' ':
            theBoard[move] = turn

        else:
            print("That space is already taken. Try again.")
            continue
    else:
        print("Invalid move. Try again.")
        continue

    winner = checkWinner(theBoard)
    if winner:
        printBoard(theBoard)
        print(f"Player {winner} wins!")
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    printBoard(theBoard)
    print("It's a draw!")


