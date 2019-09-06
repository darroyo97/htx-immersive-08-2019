import board
import turn
import win
#import location
#----Global Varibles----

game_continues = True
winner = None


#Plays the game
def play_game():
    # while the game is still goign
    while game_continues:
        #handles a single turn of player
        turn.handle_turn(turn.current_player)
        #checks if game has ended
        win.check_winner()
        #flips players
        turn.player_switch()
    #game has ended
    if winner == 'X' or winner == 'O':
        print(winner + "won!")
    elif winner == None: 
        print("Tie!")  



play_game()