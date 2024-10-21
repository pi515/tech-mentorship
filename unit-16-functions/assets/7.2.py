# ex 7.2 - impure function

def impure_noice(list1, list2):
    list1.extend(list2)
    return list1


no = ['n', 'o']
ice = ['i', 'c', 'e']

print('no   ', no)
print('ice  ', ice)
print('noice', impure_noice(no, ice))
print('noice', impure_noice(no, ice))
print('noice', impure_noice(no, ice))
