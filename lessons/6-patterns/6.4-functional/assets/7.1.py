# ex 7.1 - pure function

def pure_noice(list1, list2):
    return list1 + list2


no = ['n', 'o']
ice = ['i', 'c', 'e']

print('no   ', no)
print('ice  ', ice)
print('noice', pure_noice(no, ice))
print('noice', pure_noice(no, ice))
print('noice', pure_noice(no, ice))
