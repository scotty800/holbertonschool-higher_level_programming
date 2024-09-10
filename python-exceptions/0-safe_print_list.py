#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index2 = 0 
    try:
        for index1 in range(x):
            print("{}".format(my_list[index1], end=""))
            index2 += 1
    except IndexError:
        pass 
    print()
    return index2
