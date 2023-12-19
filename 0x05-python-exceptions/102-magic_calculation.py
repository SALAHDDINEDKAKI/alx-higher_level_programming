#!/usr/bin/python3

def magic_calculation(a, b):
    results = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            results += (a ** b) / i
        except ZeroDivisionError:
            results = float('inf')
        except Exception as e:
            results = b + a
            break

    return results
