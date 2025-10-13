# Hangman without the hangman
# Author: Ryan McDaniel

from subprocess import call

join = lambda s, xs: s.join(xs)

secretString = input('secretString:')

# while len(secretString) > 10:
#   secretString = input(
#     'secretString must be less than or equal to 10 characters:')

call('clear')

renderString = join('', (' ' for x in secretString))
indexString = list(map(lambda idx: str(idx), range(len(secretString))))

lengthIsKnown = False

livesLeft = 10

replaceGuess = lambda g: lambda s, r: s if s == g else r
spaced = lambda cs: ()

print("Guess a letter in the secretString:")
while (livesLeft > 0) & (renderString != secretString):
    guessed = input('> ')
    call('clear')
    print('>', guessed)
    print(renderString)

    if len(guessed.split('[')) > 1:
        try:
            indexAccess = guessed.split('[')[1].split(']')[0]
            indexAccessInt = int(indexAccess)
            print(secretString[indexAccessInt], '\n')
        except:
            livesLeft -= 1
    elif len(guessed.split('len(')) > 1:
        try:
            print(len(secretString), '\n')

            curString = join(
                '',
                map(lambda charN, r: ' ' if charN == ' ' else r
                if r != ' ' else '_', secretString, renderString))
            renderString = curString

            lengthIsKnown = True
        except:
            livesLeft -= 1
    else:
        try:
            guessedLetter, _, _ = guessed.split(' ')
            guessedLetter = guessedLetter.replace('\'', '')
            print(guessedLetter in secretString, '\n')

            curString = join(
                '', map(replaceGuess(guessedLetter), secretString, renderString))

            livesLeft -= 0 if renderString != curString else 1

            renderString = curString
        except:
            livesLeft -= 1

    print(join(' ', (c for c in renderString)))
    if lengthIsKnown:
        index1d = (str(c) for c in indexString)

        index2d = [[ten[0] if len(ten) > 1 else ' ' for ten in indexString],
                   [one[1] if len(one) > 1 else one[0] for one in indexString]]
        print('')
        print(join(' ', index2d[0]))
        print(join(' ', index2d[1]))

        # print(join(' ', (str(b)[0] for b in indexString)))
        # print(join(' ', (b for b in indexString)))

    print('\nLives left:', str(livesLeft), '\n')
    print('Next guess:')

if renderString == secretString:
    maxLen = 3
    print('\n'.join(
        list(
            map(
                lambda x: "!!    " + x * "    " + "N O I C E" +
                          (maxLen - x) * "    " + "!!\n", range(0, maxLen)))))
