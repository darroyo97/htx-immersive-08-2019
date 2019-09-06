#this where player will input where they want to move to which space)
import board
#import global
game_continues = True
winner = None

def check_if_game_over():
    check_for_winner()

def check_for_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
def check_rows():
  global game_still_going
  row_1 = board.board[0] == board.board[1] == board.board[2] 
  row_2 = board.board[3] == board.board[4] == board.board[5] 
  row_3 = board.board[6] == board.board[7] == board.board[8] 
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    return board.board[0] 
  elif row_2:
    return board.board[3] 
  elif row_3:
    return board.board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board.board[0] == board.board[3] == board.board[6]
  column_2 = board.board[1] == board.board[4] == board.board[7] 
  column_3 = board.board[2] == board.board[5] == board.board[8] 
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board.board[0] 
  elif column_2:
    return board.board[1] 
  elif column_3:
    return board.board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board.board[0] == board.board[4] == board.board[8] 
  diagonal_2 = board.board[2] == board.board[4] == board.board[6]
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board.board[0] 
  elif diagonal_2:
    return board.board[2]
  # Or return None if there was no winner
  else:
    return None