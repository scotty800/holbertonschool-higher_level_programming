#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.keys())
    for index in sorted_dic:
        print("{}: {}".format(index, a_dictionary[index]))
