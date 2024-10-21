# import modules
import os

# Clears shell terminal
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

# Contains information about the player
class Player:

  def __init__(self, name):
    self.name = name
    self.score = 0


# Program Start
# Player enters name
playerName = input('Please enter your name\n')
p1 = Player(playerName)
print('Welcome ' + p1.name + '! Let\'s start farming!')

# Press key to enter game
input('Press any key to continue...')
clear()

userIn = ''
# Game loop
while userIn != 'quit' and userIn != 'q':
  # Print player info at top of screen
  print(p1)

  # Print plant information
  print('Plant: ')
  print(' |/')
  print('\| ')
  print(' |/')
  print('\|/')
  print('\| ')
  print(' | ')
  print('\n')

  # Print commands available to user
  print('Commands:')
  print('harvest / h - harvest current plant')
  print('spray / s - spray plant with herbicide')
  print('quit / q - quit game')
  print('\n')

  # Execute command on user input
  userIn = input('Input: ')
  if userIn == 'harvest' or userIn == 'h':
    p1.score += 10
  elif userIn == 'spray' or userIn == 's':
    pass
  else:
    print('Invalid command')

  # Clear terminal
  clear()
