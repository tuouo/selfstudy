#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {"Lily":90, "Bob":84, 'Jack':88}
print(d, d['Bob'])
d['jack'] = 67
print(d, d.get('jack'), d.get('jack', -1), d.get('haha', -3))
d.pop('jack')
d['Jack'] = 76
print(d, d.get('jack'), d.get('jack', -3))
for dn in d:
    print(dn)
print()

s = set([2, 3, 3, 2, 1, 5, 2])
print(s, len(s))
s.add(3)
print(s, len(s))
s.add('a')
print(s, len(s))
s.add(4)
print(s, len(s))
s.remove(2)
print(s, len(s))
list = [1, 2, 3]		# [1, 2, 3, [4, 5]] error
s1 = set(list)
print('s1', s1, len(s1))
s2 = s
print('s2', s2, len(s2))
print(s1 & s2, s1 | s2)

