#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(bool(0))
print(abs(-1))
#print(abs('a'))
print(max(2, 4, 21, 45, 39, 3.33))
print(max)
a = max 
print(a)
print(a(2, 4, 21, 45, 39, 3.33))

def nop(flag):
    if flag == 1:
        pass
    elif flag == 2:
        return
nop("nothing")
		
def self_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return x, -x
print(self_abs(-5))
#print(self_abs('a'))

def enroll(name, gender, age = 6, city = 'Hangzhou'):
    print('name:', name, "\tgender", gender, "\tage", age, "\tcity", city)
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

def append_end(L = ['end']):	# very very needed avoid
    L.append('END')
    return L
print(append_end(['x', 'y', 'z']))
print(append_end())
print(append_end())

def append_end2(L = None):	# very very needed avoid
    if L is None:
        L = [ ]
    L.append('END')
    return L
print(append_end2())
print(append_end2())

