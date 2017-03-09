#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def function():
    return 1
print(function)
function = 2
print(function)

def add(x, y, function):
    return function(x) + function(y)
print(add(-3, 7, abs))

num = [1, 3, 5, 7, 9]
print(list(map(str, num)))
print(list(map(lambda x: x * x, num)))

from functools import reduce
def fn(x, y):
    return 10 * x + y
print(reduce(fn, num))
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
print(reduce(fn, map(char2num, '26373')))

def str2int(s):
    return reduce(lambda x, y: 10 * x + y, map(char2num, s))
print(str2int('37273'))

name = ['lIly', 'LISa', 'barT']
def normalize(name):
    return name.lower().title()
print(list(map(normalize, name)))

def prod(L):
    return reduce(lambda x, y: x * y, L)
print(prod(num))

def str2float(s):
    a = s.split('.')
    return int(a[0]) + int(a[1]) / (10 ** len(a[1]))
    #return str2int(a[0]) + str2int(a[1]) / (10 ** len(a[1]))
print(str2float('124.56'))