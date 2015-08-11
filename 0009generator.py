#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def gen():
    print("step 1")
    yield 1
    print("step 2")
    yield(2)						# doesnot matter
    print("step 3")
    yield 5
g = gen()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))						# StopIteration

def fibGen(num):					# num: p i
    n, a, b = 0, 0, 1
    while n < num and n < 100:		# n < 100 --> end
        yield b
        a, b, n = b, a + b, n + 1
    return "OK."
fg = fibGen(6)
while True:
    try:
        x = next(fg)
        print(x, ' ' , end = '')
    except StopIteration as e:
        print('gen return value', e.value)
        break;

def trianglesGen(num):					# num: p i
    l = [1]
    n = 0
    while n < num and n < 100:
        yield l
        i, pre = 1, 1
        for x in l[1:]:
            l[i] = x + pre
            pre, i = x, i + 1
        l.append(1)
        n += 1	
for i in trianglesGen(4):
    print(i)
            
		
