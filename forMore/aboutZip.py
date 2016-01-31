#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A = [1, 2, 3]
a = [1, 2, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c']
zz = [(1, 'a'), (2, 'b'), (3, 'c')]
z = list(zip(a, b))    # zip(a, b) is zip object, only use once
aa, bb = zip(*z)
print(all((tuple(A) == aa, tuple(b) == bb, z == zz))) # True


ato2 = list(zip(*([iter(a)] * 2)))
# print(type(iter(a)), iter(a))
# print(type([iter(a)]), [iter(a)])
ato2o = [(1, 2), (3, 4), (5, 6)]
ato2l = list(zip(a[::2], a[1::2]))
group_adjacent = lambda a, n: list(zip(*([iter(a)] * n)))
group_adjacent2 = lambda a, n: list(zip(*(a[i::n] for i in range(n))))
print(ato2 == ato2o == ato2l == group_adjacent(a, 2) == group_adjacent2(a, 2))