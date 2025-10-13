# ex 7.3 - higher order printing function

# 1. What does this code do?
# 2. How can we make this more readable?

def hoc_noice(style):
    def pad(num):
        padding = []
        for _ in range(0, num):
            padding.append(' ')
        return ''.join(padding)

    noIce = ['n', 'O', 'i', 'C', 'e', '!']

    for i in range(0, len(noIce)):
        print(pad(i), style(noIce[i]))


hoc_noice(lambda char: char.lower())
hoc_noice(lambda char: char.upper())