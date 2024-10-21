# ex 0 - function definition / interface
def myFn(param1, param2, paramN):  # (...parameters)
    print(param1)  # function body
    print(param2)
    print(paramN)
    return param1 + param2 + paramN  # return statement (optional)


# function call
returned = myFn('Functions ', 'are ', 'NOICE')  # (...arguments)
print(returned)