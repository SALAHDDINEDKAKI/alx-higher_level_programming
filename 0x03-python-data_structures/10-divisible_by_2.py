#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiplication = []
    for integer in range(len(my_list)):
        if my_list[integer] % 2 == 0:
            multiplication.append(True)
        else:
            multiplication.append(False)
    return multiplication
