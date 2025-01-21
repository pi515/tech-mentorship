import random

# Let's test your knowledge of everything you have learned so far!
# Earlier, you learned to use the random library to simulate a game of rock, paper, scissors.
# Now write a function that simulates a two-player game where you are playing against a friend
# Plot twists:
#   1. Because your friend is super competitive, the game must go on until your friend wins
#   2. The function must return your friend's winning move as a string
#   3. Bonus: In the same string statement, also include the number of games it took for your friend to win.
# Hint: this exercise will test your knowledge of loops, booleans and use of the random library
def rock_paper_scissors() -> str:
    friend_wins = False
    moves = ["rock", "paper", "scissors"]
    num_games = 0
    # Your code here:
    
    return "" # Replace this line with a string statement that contains your friend's winning move

result = rock_paper_scissors()
print(result) 
# expected: A string statement containing your friend's winning move 
# optional: The string also outputs the number of games it took for your friend to win