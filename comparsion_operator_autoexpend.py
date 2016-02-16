#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You can chain together comparison operators 
and they are automatically expanded out into the pairwise comparisons

all comparison operations in Python have the same priority
"""
""" why 1 in [0, 1] == True return False """
print(1 in [0, 1] == True)  # False
print(1 in [0, 1])  # True
print((1 in [0, 1]) == True)  # True
# print(1 in ([0, 1] == True))  # TypeError
"""automatically expanded
1 in [0, 1] == True means (1 in [0, 1]) and ([0, 1] == True)
"""

# same priority
print(0 < 0 == 0) # False