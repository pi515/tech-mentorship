import random
# Exercise 1: Import the math library, using Line 1 as a reference
# Your code here:
import math

# Exercise 2: 
# You saw the `random.randint()` method in an earlier example
# How would you use the method to simulate a six-sided dice roll?
# Your code here:
roll = random.randint(1, 6)
print(roll)

# Exercise 3: 
# Now it's time to read the documentation for random:
# https://docs.python.org/3/library/random.html#functions-for-sequences
# What method in random would you use to simulate a game of rock, paper, scissors?
# Hint: No need to scroll too far
# Your code here:
moves = ["rock", "paper", "scissors"]
move = random.choice(moves)
print(move)