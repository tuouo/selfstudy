#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
True and False can be used as integer values
True, False -> 1, 0 : not recommend
But True and False are keywords in python3
"""
a = 7
print(isinstance(a, int) + (a <= 7))
print(["is odd", "is even"][a % 2 == 0])
print(int(True), int(False))
print(1 == True, 0 == False)    # True True
print(2 == True, -1 == False)   # False False

from timeit import timeit
def test_true():
    count = 1000
    while True:
        if count < 0:
            break
        count -= 1

def test_1():
    count = 1000
    while 1:
        if count < 0:
            break
        count -= 1

# on my surface pro 3
# test_true is about 78.83515609636538 seconds
# test_1 is about 79.09397927801915 seconds
# so, in python3 there is no necessary to replace True with 1
print(timeit(test_true, number = 1000000))
print(timeit(test_1, number = 1000000))