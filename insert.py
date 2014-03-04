"""
A script to perform what could normally be done with l.insert(i, x)
...just because.
"""


l = [1, 2, 3, 4, 5, 7, 8, 9, 10]


def find_index(l, missing):
    if missing > l[-1]:
        last = l[-1]
        return l.index(last)
    for num in l:
        if num < missing:
            pass
        elif num > missing:
            return l.index(num)

find_index(l, 6)
find_index([1, 2, 3, 4, 5, 6, 7, 9, 10], 8)
find_index([2, 3, 4, 5, 6, 7, 8, 9, 10], 1)  # first element
find_index([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)  # last element


def shift(l, shift_index):
    l.append(' ')
    for i in reversed(range(shift_index, len(l))):
        l[i] = l[i - 1]
    return l

shift([11, 22, 33, 44, 55, 66, 77, 99, 100], 7)


def insert(l, missing):
    print "INSERTION:"
    found_index = find_index(l, missing)
    print found_index
    shifted_list = shift(l, found_index)
    print shifted_list
    l[found_index] = missing
    print l

insert([1, 2, 3, 4, 5, 6, 7, 9, 10], 8)
