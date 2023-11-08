#!/usr/bin/python3

def search_replace(my_list, search, replace):
    test = my_list.copy()
    for i, j in enumerate(test):
        if j == search:
            test[i] = replace
    return test
