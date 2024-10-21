# Functions - Exercise 3
#
#   What's going on here???
#

def printSquare():
    def square(num):
        num = 5
        return num ** 2

    myNumber = 10
    print(square(num))

printSquare()

print(myNumber)