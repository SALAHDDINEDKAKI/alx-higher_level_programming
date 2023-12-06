#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    den1 = 0

    for tup2 in my_list:
        number += tup2[0] * tup2[1]
        den1 += tup2[1]
    return number / den1
