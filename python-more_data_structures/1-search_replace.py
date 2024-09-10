#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if 0 <= search < len(my_list):
        my_list[search] = replace
        return(my_list)