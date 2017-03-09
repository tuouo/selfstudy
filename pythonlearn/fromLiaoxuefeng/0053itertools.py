#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
# function in itertools return Iterator, only if in "for", will count
natuals = itertools.count(1)	# from 1, step by 1
for n in natuals:				# Iterator
    if n > 100:
        break;
    print(n, ' ', end = '')
print()

cycles = itertools.cycle('asdf')
count = 1
for i in cycles:
    if count > 100:
        break;
    count += 1
    print(i, ' ', end = '')	
print()

repeats = itertools.repeat('q', 10)
for i in repeats:
    print(i, ' ', end = '')
print()
	
# method helps up to get limited sequence
natuals = itertools.count(1)			# !!! natuals was used, must define again !!!
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print(n, ' ', end = '')
print("\n################################################")
	
for i in itertools.chain('ABC', 'XYZ'):
    print(i, ' ', end = '')	
print()

story = 'TtteEeeTT'
for key, group in itertools.groupby(story):
    print(key, list(group))
for key, group in itertools.groupby(story, lambda c: c.upper()):
    print(key, list(group))
