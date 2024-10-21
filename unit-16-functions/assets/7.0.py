# ex 7.0 - idempotent function

def noice(list1, list2):
    return list1 + list2


no = ['n', 'o']
ice = ['i', 'c', 'e']

print('no   ', no)
print('ice  ', ice)
print('noice', noice(no, ice))
print('noice', noice(no, ice))
print('noice', noice(no, ice))
