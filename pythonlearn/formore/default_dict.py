#!/usr/bin/env python3
# -*- coding: utf-8 -*-
names = ['james', 'peter', 'simon', 'jack', 'john', 'lawrence', 'li']


group = {}
for name in names:
    group.setdefault(len(name),[]).append(name)


from collections import defaultdict
group2 = defaultdict(list)
for name in names:
    group2[len(name)].append(name)


from itertools import groupby
group3 = {k:list(v) for k, v in groupby(names, len)}

print(group)
print(group2)
print(group3)
print(group == group2)
print(group == group3)