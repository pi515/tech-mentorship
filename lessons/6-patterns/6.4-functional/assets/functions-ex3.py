# Functions - Exercise 3
#
#   Is this allowed???
#

zeroToNine = [0,1,2,3,4,5,6,7,8,9]


def getSquareLoop():
    square = lambda x: x ** 2

    loop = lambda inputList: [square(x) for x in inputList]

    return loop

squareLoop = getSquareLoop()

print(squareLoop(zeroToNine))