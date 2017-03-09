#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
import json

tree = lambda : defaultdict(tree)

users = tree()
users['1']['2'] = "lily"
users['1']['3'] = "dick"
print(users)
print(json.dumps(users))

num = tree()
num['0']['1']['2']['3']['4']['5']['6']
num['0']['1']['2']['3']['4']['7']['8']
num['0']['1']['2']['3']['9']['10']['11']
num['a']['0']['2']['4']
num['a']['b']['2']['4']
num['a']['b']['2']['5']
print(json.dumps(num))

def add(t, keys):
    for key in keys:
        t = t[key]

add(num, '0,1,2,3,4,5,6,7'.split(','))  # 7 is new as a child of '6'
print(json.dumps(num))
