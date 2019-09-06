import board
from tictactoe import game_continues
from tictactoe import winner

def check():
    check_winner()

def check_winner():
    global winner
    game_winner = check_board()
    if game_winner:
        winner = game_winner
    else:
        winner = None

#check for winner
def check_board():  
    global game_continues
    win1 = board.board[0] == board.board[1] == board.board[2]
    win2 = board.board[3] == board.board[4] == board.board[5]
    win3 = board.board[6] == board.board[7] == board.board[8]
    win4 = board.board[0] == board.board[3] == board.board[6]
    win5 = board.board[1] == board.board[4] == board.board[7]
    win6 = board.board[2] == board.board[5] == board.board[8]
    win7 = board.board[2] == board.board[4] == board.board[6]
    win8 = board.board[0] == board.board[4] == board.board[8]
    if win1 or win2 or win3 or win4 or win5 or win6 or win7 or win8:
        game_continues = False
    if win1:
        return board.board[0]
    elif win2:
        return board.board[3]
    elif win3:
        return board.board[6]
    elif win4:
        return board.board[0]
    elif win5:
        return board.board[1]
    elif win6:
        return board.board[2]
    elif win7:
        return board.board[2]
    elif win8:
        return board.board[0]


#def check_tie():
    #return