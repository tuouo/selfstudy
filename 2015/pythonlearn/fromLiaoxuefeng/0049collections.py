#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
Point = namedtuple('point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y, p)	# p.x = 3-->error, can't set attribute
print(isinstance(p, Point), isinstance(p, tuple))
# other use of namedtuple
Circle = namedtuple('O', ['x', 'y', 'r'])

from collections import deque		# both side list
q = deque(['a', 'b', 'c'])
print(q)
q.pop()
q.append('x')
q.popleft()
q.appendleft('y')
print(q)

from collections import defaultdict
dd = defaultdict(lambda: 'Null')
dd['kay1'] = '123'
print(dd['kay1'], dd['kay2'])

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
print(od, od.keys())		# order by insert order
od['e'] = 4
od['e'] = 7
print(od)
od.popitem()
print(od)
od.popitem(last = False)
print(od)

class LastUpdateOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderDict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.capacity:
            last = self.popitem(last = False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
luod = LastUpdateOrderDict(3)
luod['a'] = 1
luod['s'] = 7
luod['d'] = 3
print(luod)
luod['d'] = 2
print(luod)
luod['a'] = 7
print(luod)
luod['f'] = 9
print(luod)

from collections import Counter
c = Counter()					# no order
for ch in 'programming':
    c[ch] += 1
print(c)