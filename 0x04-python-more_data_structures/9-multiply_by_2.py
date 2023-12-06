#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multi = a_dictionary.copy()
    list_key = list(multi.keys())
    
    for i in list_key:
        multi[i] *= 2
    return multi
