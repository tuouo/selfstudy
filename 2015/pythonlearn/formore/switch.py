#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Using a Dictionary in place of a 'switch' statement """
def f(n):
    return {
        'a': lambda x: x * 5,
        'b': lambda x: x + 3,
        'c': lambda x: x - 1,        
    }.get(n, lambda x: x)

print(f('a'))
print(f('3'))
print(f('a')(2))
print(f('3')(2))