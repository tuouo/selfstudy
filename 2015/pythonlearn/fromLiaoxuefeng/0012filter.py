#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_odd(n):
   return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print(list(filter(is_palindrome, range(1, 100))))

# filter decides keep or not, not change things, even if things changed in function
strs = ['a', '', None, 'c   ', ' ', 'd']	#be carefully, do not use name like str
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, strs)))
strsNotEmpty = list(map(not_empty, strs))
print(strsNotEmpty)
print([i for i in strsNotEmpty if i])
print([i for i in strsNotEmpty if i == True])

def _odd_iter():
    n = 3
    while True:
        yield n
        n += 2
def _not_divisible(n):
    return lambda x: x % n > 0
def primes(num):
    yield 2
    it = _odd_iter()			 #need (), don't lost
    n = next(it)
    while n < num:
        yield n
        it = filter(_not_divisible, it)
        n = next(it)
print([i for i in primes(100)])

def primes2():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible, it)
for i in primes2():
    if i < 100:
        print(i, ' ', end ='')
    else:
        break