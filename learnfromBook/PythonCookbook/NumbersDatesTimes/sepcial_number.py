#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from fractions import Fraction
import cmath

a, b, c = float('inf'), float('-inf'), float('nan')
print(type(a), a, type(b), b, type(c), c)
print(math.isinf(a), math.isnan(c), a == a, c == c)
print(a + 45, a * 10, 10 / a, a / a, a + b, a == float('inf'))
print(c + 45, c * 10, 10 / c, c == float('nan'), c is float('nan'))

a, b = Fraction(5, 4), Fraction(7, 16)
print(a + b, a * b)
c = Fraction(3, 8) * Fraction(7, 5)
print(c.numerator, c.denominator, float(c), c.limit_denominator(8), c.limit_denominator(64))
print(Fraction(*4.625.as_integer_ratio()), Fraction(4.625), Fraction(" -4.625 \t\n"))

a, b = complex(2, 4), 3 - 5j
print(a, a.real, a.imag, a.conjugate(), a.conjugate)
print(b, a + b, a * b, a / b, abs(a))
print(cmath.sin(a), cmath.cos(a), cmath.exp(a))
print(cmath.sqrt(-1))
