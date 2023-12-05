#!/usr/bin/python3
a = 89
b = 10
if a == 89 and b == 10:
    c = a # c = 89
    a = b # a = 10
    b = c # b = 89
print("a={:d} - b={:d}".format(a, b))
