#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calling different functions with same arguments based on condition
"""
def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

condition = True
print((multiply if condition else subtract)(1, 1))