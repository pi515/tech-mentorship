# ex 1 - label the 'anatomy' of these functions

print(type(print()))  # ?
print(type(print))    # ?

# 0. ?
renamedPrint = print


# 1. ?
def myFirstFn(delimiter, noIce):  # 2. delimiter, noIce - ?
    singleStr = ''.join(noIce)  # 3. ?

    letters = [x for x in singleStr]

    joined = delimiter.join(letters)

    capitalized = joined.upper()

    return capitalized  # 4. ?, do functions always have this?


# 5. ?
def mySecondFn(str):  # 6. str - ?
    renamedPrint(str)  # 7. ?
    # 8. what type of function is this?


delimiter = ' '
noIce = ['no', 'Ice']

# 9. ?
myFirstFunctionOutput = myFirstFn(delimiter, noIce)  # 10. delimiter, noIce - ?

# 11. ?
mySecondFn(myFirstFunctionOutput)  # 12. myFirstFunctionOutput - ?
