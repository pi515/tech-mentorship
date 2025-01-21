import random

# Let's test your knowledge of everything you have learned so far!
# Earlier, you learned to use the random library to simulate a game of rock, paper, scissors.
# Now write a function that simulates a two-player game where you are playing against a friend
# Plot twists:
#   1. Because your friend is super competitive, the game must go on until your friend wins
#   2. The function must return a string that contains your friend's winning move
#   3. Bonus: In the same string statement, also include the number of games it took for your friend to win.
# Hint: this exercise will test your knowledge of loops, booleans and use of the random library
def rock_paper_scissors() -> str:
    friend_wins = False
    moves = ["rock", "paper", "scissors"]
    num_games = 0

    while friend_wins is False:
        your_move = random.choice(moves)
        friend_move = random.choice(moves)
        friend_wins = (your_move == "rock" and friend_move == "paper") or (your_move == "scissors" and friend_move == "rock") or (your_move == "paper" and friend_move == "scissors")
        num_games += 1
    
    return f"Your friend finally won with {friend_move} vs your {your_move}! It took {num_games} game(s) for your friend to win"

result = rock_paper_scissors()
print(result) 
# expected: A string outputting your friend's winning move 
# optional: The string also outputs the number of games it took for your friend to win