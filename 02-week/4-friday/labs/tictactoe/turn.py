import board
def turn():
    position = int(input('Choose a spot.'' From 0-8:'))
    board.board[position] = 'X'
    board.show()



