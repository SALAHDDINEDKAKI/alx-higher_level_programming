#!/usr/bin/env python3

def no_c(my_string):
    duplication = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(duplication))
