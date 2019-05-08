

board = [' ' for x in range(10)]

def insertLetter(letter, position):
    board[position] = letter

def spaceIsFree(position):
    return board[position] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter) or \
           (board[1] == letter and board[5] == letter and board[9] == letter) or \
           (board[3] == letter and board[5] == letter and board[7] == letter)

def playerMove():
    run = True
    while run:
        move = input('Please select a position between 1-9 to place an "X" on the board:')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry John, this space is already full')
            else:
                print('Please type a number within the range, John!')
        except:
            print('Please type an actual number, John!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 'O']
    move = 0

    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7 ,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(list):
    import random
    length = len(list)
    randomNumber = random.randrange(0, length)
    return list[randomNumber]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Moose\'s nut-tacular Tic-Tac-Toe')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry John, O\'s won this time')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game, Johns!')
            else:
                insertLetter('O', move)
                print('Computer placed an "O" in position ', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time, good job John')
            break

    if isBoardFull(board):
        print('Game over, Johns!')

main()