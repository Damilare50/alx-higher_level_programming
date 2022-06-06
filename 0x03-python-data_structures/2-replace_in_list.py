#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list

    x = 0
    while x < len(my_list):
        if x == idx:
            my_list[idx] = element
        x += 1
    return my_list
