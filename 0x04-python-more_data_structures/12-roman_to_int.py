#!/usr/bin/python3
def to_subtract(list_num):
    to_sub1 = 0
    max_list = max(list_num)

    for n1 in list_num:
        if max_list > n1:
            to_sub1 += n1

    return (max_list - to_sub1)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())

    number = 0
    last_rom = 0
    list_num = [0]

    for ch1 in roman_string:
        for r_num1 in list_keys:
            if r_num1 == ch1:
                if rom_num.get(ch1) <= last_rom:
                    number += to_subtract(list_num)
                    list_num = [rom_num.get(ch1)]
                else:
                    list_num.append(rom_num.get(ch1))

                last_rom = rom_num.get(ch1)

    number += to_subtract(list_num)

    return (number)
