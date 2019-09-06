import board
#this fucntion places x 

#Whos turn it is 
current_player = 'X'

#this fucntion places input
def handle_turn(player):
    position = int(input('Choose a spot.'' From 0-8:'))
    board.board[position] = 'X'
    board.show()
#this swtiches players
def player_switch():
    return



