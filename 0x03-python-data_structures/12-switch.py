#!/usr/bin/python3
a = 89
b = 10
if a == 89 and b == 10:
    a = 89
    b = 10
    a, b = b, a
print("a={:d} - b={:d}".format(a, b))
