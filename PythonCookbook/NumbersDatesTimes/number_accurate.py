#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal
from decimal import localcontext
import math

print(round(1.5, 0), round(2.5, 0), round(3.5, 0), round(4.5, 0))
print(round(15, -1), round(25, -1), round(35, -1), round(45, -1))
print(3.2 + 1.1)
a, b = Decimal("3.2"), Decimal("1.1")
print(a + b, a + b == Decimal("4.3"))

print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
    ctx.prec = 30
    print(a / b)

nums = [1.11e+18, 1, -1.11e+18, 2]
print(sum(nums), math.fsum(nums))
