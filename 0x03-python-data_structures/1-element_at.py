#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None

    x = 0
    pos = 0
    while x < len(my_list):
        if x == idx:
            pos = my_list[idx]
            break
        x += 1
    return pos
