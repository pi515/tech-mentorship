# ex 8 - what kind of function is this???
# your choices are (hint: they can be multiple ones of these!):
#   1. idempotent
#   2. pure
#   3. impure
#   4. higher order
#   5. stateful (lifecycle)


# =============================================
# example0
# adding 2 numbers together
# =============================================
def add(num1, num2):  # your answer:
    return num1 + num2


def example0():
    print(add(2, 2))
    print(add(2, 2))


example0()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example1
# creating a multiplier
# =============================================
def example1():
    def init_multiplier(multiplier):  # your answer:
        return lambda num: num * multiplier  # your answer:

    daily_double = init_multiplier(2)
    print(daily_double(500))
    print(daily_double(500))


# example1()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example2
# counting with a global variable
# =============================================
global_counter = [0]


def count_global():  # your answer:
    global_counter[0] += 1
    return global_counter[0]


def example2():
    print(count_global())
    print(count_global())


# example2()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example3
# counting with an input parameter
# =============================================
def example3():
    def count(counterParam):  # your answer:
        counterParam[0] += 1
        return counterParam[0]

    counter = [0]
    print('example3', count(counter))
    print('example3', count(counter))
    print('example3', count(counter))
    print('example3', count(counter))


# example3()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example4
# append an element to a list
# =============================================
def example4():
    def append(myList, nextElement):  # your answer:
        myList.append(nextElement)
        return myList

    no = ['n', 'o', 'i', 'c']
    print(append(no, 'e'))
    print(append(no, 'e'))
    print(append(no, 'e'))
    print(append(no, 'e'))


# example4()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example5
# append an element to a list
# =============================================
def example5():
    def append(myList, nextElement):  # your answer:
        return myList + [nextElement]

    no = ['n', 'o', 'i', 'c']
    print(append(no, 'e'))
    print(append(no, 'e'))
    print(append(no, 'e'))
    print(append(no, 'e'))


# example5()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example6
# counter with local variables
# =============================================
def example6():
    def init_counter():  # your answer:
        counter = [0]

        def count_inner():  # your answer:
            counter[0] += 1
            return counter[0]

        return count_inner

    counter_1 = init_counter()
    counter_2 = init_counter()
    print('init counter_1', counter_1)
    print('increment counter_1', counter_1())
    print('increment counter_1', counter_1())
    print('init counter_2', counter_2)
    print('increment counter_2', counter_2())
    print('increment counter_2', counter_2())


# example6()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example7
# do some math on 2 numbers
# =============================================
def example7():
    def doMath(fn, num1, num2):  # your answer:
        operation = fn
        return operation(num1, num2)

    print(doMath(add, 2, 2))
    print(doMath(add, 2, 2))


# example7()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example8
# finding max with a loop function
# =============================================
def example8():
    def findMax(nums):  # your answer:
        max = 0
        for i in range(0, len(nums)):
            if nums[i] > max:
                max = nums[i]
        return max

    print(findMax([1, 2, 3, 9, 0]))
    print(findMax([1, 2, 3, 9, 0]))


# example8()  # (un)comment while you are(n't) working here for clearer terminal output


# =============================================
# example9
# making a custom variable with functions
# this is a foundational example for a future lesson :)
# =============================================
def example9():
    def init_var(initial):  # your answer:
        var = [initial]

        def set(next):  # your answer:
            var[0] = next
            return var[0]

        def get():  # your answer:
            return var[0]

        return get, set

    getNoice, setNoice = init_var("noice")
    print(getNoice())
    print(getNoice())
    print(setNoice("No Ice"))
    print(setNoice("No Ice"))
    print(getNoice())
    print(getNoice())
    print(setNoice("NOICE"))
    print(setNoice("NOICE"))
    print(getNoice())
    print(getNoice())

# example9()  # (un)comment while you are(n't) working here for clearer terminal output
