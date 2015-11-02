#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
s = b'bidnary\x00staring'
scode = base64.b64encode(s)
print(scode)
sOrigin = base64.b64decode(scode)
print(sOrigin)

# in case '+'&'/' in url
s = b'i\xb7\x1d\xfb\xef\xff'
scode = base64.b64encode(s)
print(scode)
scode = base64.urlsafe_b64encode(s)
print(scode)
sOrigin = base64.urlsafe_b64decode(scode)
print(sOrigin)

# also, we can define The order of 64 chars

def no_equal_b64decode(s):
    euqalNum = (-len(s)) % 4
    s += euqalNum * '='
    return base64.b64decode(s)
	
print(no_equal_b64decode('YWJjZA=='))
print(no_equal_b64decode('YWJjZA'))