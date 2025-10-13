# ex 4 - functions with default parameters
# can you find what's wrong with these function definitions?


def print1(str = 'NOICE'): # param = defaultValue, hint: order matters!
    print(str)

def print2(str1, str2 = 'NOICE')
    print(str1, str2)

def print3(str1, str2 = 'VERY', str3, str4 = 'JOB'):
    print(str1, str2, str3, str4)

print1()
print2('VERY')
print3('VERY')