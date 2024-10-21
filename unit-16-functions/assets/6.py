# Do not touch!
def test(case, expr):
    if expr == True:
        print('test', case, '= PASS')
    else:
        print('test', case, '= KEEP TRYING :)')


# ex 6 - writing your own function

# Python's math system does not like division by zero...
# Using any of the python logic and syntax you've learned so far,
# do the following:
#   1. Divide num1 by num2 and return the result
#   2. If num1 is not a number, try converting it to a number
#   3. If num1 cannot be converted to a number, return num2
#   4. If num2 is 0, return "Infinity"
#   5. If num2 is not provided, default to 1
def div(num1, num2):
    # Write your code here
    pass


# Get all these statements to print PASS!
test(0, div(0, 10) == 0)
test(1, div(10, 5) == 2)
test(2, div("0", 2) == 0)
test(3, div("0", 0) == 'Infinity')
test(4, div(10, 0) == 'Infinity')
test(5, div([10], 0) == 0)
test(6, div(10) == 10)
