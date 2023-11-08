#!/usr/bin/python3

def uniq_add(my_list=[]):
    addition = 0
    unik = set(my_list)
    for i in unik:
        addition += i
    return addition
