# ex 5 - functions inside functions, what???
# can you figure out what's wrong?

def outside():
    print('first')

    def inside():
    print('third')
        return 'fourth'

    print('second')
    return inside()

print(outside())
print(inside())