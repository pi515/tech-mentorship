# ex 7.4 - stateful counting function


def initState():
    count = [0]
    def reset():
        count[0] = 0
        print(count)
    def next():
        count[0] += 1
        print(count)
    return (next, reset)


(next, reset) = initState()
next()
next()
reset()
next()
next()