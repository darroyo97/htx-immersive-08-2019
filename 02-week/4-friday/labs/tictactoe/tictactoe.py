import board
import turn
#import win
#import location
#----Global Varibles----

game_continues = True
winner = None
#THIS FUNCTION CHECKS WIN

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

#Plays the game
def play_game():
    # while the game is still goign
    while game_continues:
        #handles a single turn of player
        turn.handle_turn(turn.current_player)
        #checks if game has ended
        check_winner()
        #flips players
        turn.player_switch()
    #game has ended
    #if winner == 'X' or winner == 'O':
    #    print(winner + " won!")
    #elif winner == None: 
    #    print("Tie!")  
    if winner == 'X':
        print('Player 1 Won!')
    elif winner == 'O':
        print('Player 2 Won!')
    elif winner == None:
        print('Tie!')
    



play_game()