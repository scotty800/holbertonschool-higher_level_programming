#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return (None)
    i = my_list[0]
    for  index in my_list:
        if index > i:
            i = index
    return i
