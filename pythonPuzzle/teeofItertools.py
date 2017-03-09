#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The fast one own origin next, other get next from the queue which the fast one had genereted
"""
from itertools import tee
it1 = (x for x in range(10))
it2, it3 = tee(it1)

print(next(it2))    #0
print(next(it3))    #0
print(next(it2))    #1
print(next(it2))    #2
print(next(it3))    #1

print(next(it1))    #3
print(next(it2))    #4
print(next(it3))    #2